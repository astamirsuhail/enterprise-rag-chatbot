import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import streamlit as st
import time
import os

from src.workflows.workflow_engine import get_workflow
from src.router.intent_router import detect_intent
from src.chatbot.conversation import build_chat_history
from src.recommendation.recommendation_engine import get_recommendations
from src.router.query_router import classify_query
from src.chatbot.rag_chatbot import ask_general_gemini
from src.knowledge.document_manager import DocumentManager
from src.embeddings.embedder import create_embeddings
from src.chatbot.chatbot import (
    load_vector_db,
    retrieve_documents
)
from src.chatbot.rag_chatbot import ask_gemini

st.set_page_config(
    page_title="Volkswagen AI Assistant",
    page_icon="🚗",
    layout="wide"
)

@st.cache_resource
def initialize():

    embeddings = create_embeddings()
    db = load_vector_db(embeddings)

    return db

db = initialize()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🏢 Enterprise Knowledge AI Assistant")

    st.divider()

    st.header("Ask questions from your company knowledge base. Powered by RAG + Gemini AI.")

    st.markdown("""
    - ✈️ Business Travel
    - 🛂 Visa & Work Permit
    - 🏨 Hotel Policy
    - 💱 Forex
    - 👥 HR Policies
    - 🏢 Facility SOPs
    - 🛒 Procurement
    - 🔐 Security
    """)


    st.divider()

    st.header("System Status")

    st.success("🟢 Knowledge Base Loaded")

    
    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.subheader("Recent Searches")

    for msg in st.session_state.messages[-10:]:

        if msg["role"] == "user":

            st.write("•", msg["content"])

    st.divider()

    st.subheader("Knowledge Base")

    st.metric("Knowledge Documents", 10)

    st.metric("Indexed Chunks", 70)

# ---------------- Main Page ---------------- #

st.title("🏢 Enterprise Knowledge AI Assistant")

st.caption("Powered by LangChain • ChromaDB • Google Gemini • Streamlit")
st.subheader("⚡ Quick Questions")

col1, col2 = st.columns(2)

with col1:

    if st.button("✈️ Business Travel Policy"):
        st.session_state.quick_question = "Explain the Business Travel Policy."

    if st.button("🏨 Hotel Booking"):
        st.session_state.quick_question = "Explain the Hotel Policy."

    if st.button("💱 Forex Process"):
        st.session_state.quick_question = "Explain the Forex process."

    if st.button("🔐 Information Security"):
        st.session_state.quick_question = "Explain the Information Security Policy."

    if st.button("🛒 Procurement SOP"):
        st.session_state.quick_question = "Explain the Procurement SOP."

    

with col2:

    if st.button("🛂 Visa Process"):
        st.session_state.quick_question = "Explain the Visa process."

    if st.button("👥 HR Policies"):
        st.session_state.quick_question = "Explain HR policies."

    if st.button("🏢 Facility SOP"):
        st.session_state.quick_question = "Explain Facility SOP."

    if st.button("👤 Visitor Management"):
        st.session_state.quick_question = "Explain the Visitor Management SOP."
    
    if st.button("🏠 Work From Home"):
        st.session_state.quick_question = "Explain the Work From Home Policy."
    

if len(st.session_state.messages) == 0:

    st.info("""
# 🏢 Enterprise Knowledge AI Assistant

Ask questions from the company's internal knowledge base.

### Supported Knowledge Areas

- ✈ Business Travel
- 🏨 Hotel Booking
- 🛂 Visa Process
- 👥 HR Policies
- 🔐 Information Security
- 🛒 Procurement SOP
- 🏢 Facility Management
- 👤 Visitor Management
- 💱 Forex Policy
- 🏠 Work From Home

### Try asking

• What is the hotel booking policy?

• Explain visitor management SOP.

• What is the procurement process?

• How do I apply for business travel?

• Explain the leave policy.

• What is the work from home policy?
""")


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

typed_question = st.chat_input(
    "Ask your question..."
)

question = None

if "quick_question" in st.session_state:

    question = st.session_state.quick_question

    del st.session_state.quick_question

elif typed_question:

    question = typed_question

if question:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    start = time.time()

    intent = detect_intent(question)

    workflow = get_workflow(intent)

    # Retrieve relevant documents
    docs = retrieve_documents(
    db,
    question
    )

    query_type = classify_query(docs)

    if query_type == "COMPANY":

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        history = build_chat_history(
            st.session_state.messages
        )

        confidence = min(len(docs) * 20, 100)
        answer = ask_gemini(
            context,
            history + "\n\nCurrent Question:\n" + question
        )

        st.progress(confidence / 100)

        st.caption(f"Confidence: {confidence}%")

    else:

        answer = ask_general_gemini(
            question
        )

    end = time.time()

    st.caption(
        f"Response generated in {end-start:.2f} seconds"
    )

    
    with st.chat_message("assistant"):

        st.markdown(answer)

        # Only show workflow if company knowledge was found
        if (
            workflow
            and "I couldn't find this information" not in answer
        ):

            st.markdown("---")
            st.subheader("📋 Workflow")

            for i, step in enumerate(workflow, start=1):
                st.markdown(f"**{i}.** {step}")

        # Only show recommendations if company knowledge was found
        if "I couldn't find this information" not in answer:

            st.divider()

            st.markdown("### 💡 Related Policies")

            recommendations = get_recommendations(intent)

            cols = st.columns(2)

            for i, item in enumerate(recommendations):

                with cols[i % 2]:

                    if st.button(item, key=f"rec_{i}"):

                        st.session_state.quick_question = f"Explain {item}"

                        st.rerun()

        
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    if query_type == "COMPANY":

        st.success(
            f"✅ Knowledge Search Completed\n\nRetrieved {len(docs)} relevant knowledge chunks."
        )

        with st.expander("Retrieved Knowledge"):

            for i, doc in enumerate(docs, start=1):

                st.markdown(f"### 📄 Knowledge Chunk {i}")

                st.write(doc.page_content)

        with st.expander("📚 Sources Documents"):

            sources = set()

            for doc in docs:

                if "source" in doc.metadata:

                    sources.add(doc.metadata["source"])

            for source in sorted(sources):

                filename = os.path.basename(source)

                st.write(f"📄 {filename}")
    st.divider()

    st.caption(
        "Enterprise Knowledge AI Assistant | Built with Streamlit, LangChain, ChromaDB & Google Gemini"
    )   