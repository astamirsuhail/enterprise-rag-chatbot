from src.embeddings.embedder import create_embeddings
from src.chatbot.chatbot import load_vector_db
from src.chatbot.chatbot import retrieve_documents
from src.chatbot.rag_chatbot import ask_gemini


embeddings = create_embeddings()

db = load_vector_db(embeddings)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    docs = retrieve_documents(db, question)

    context = ""

sources = []

for doc in docs:
    context += doc.page_content + "\n\n"

    if "page" in doc.metadata:
        sources.append(doc.metadata["page"] + 1)

    answer = ask_gemini(
        context,
        question
    )

    print("\nAI:\n")
    print(answer)

print("\nSources:")

for page in sorted(set(sources)):
    print(f"Page {page}")