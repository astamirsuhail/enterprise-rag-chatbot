from src.embeddings.embedder import create_embeddings
from src.chatbot.chatbot import load_vector_db
from src.chatbot.chatbot import retrieve_documents

embeddings = create_embeddings()

db = load_vector_db(embeddings)

query = "What is Volkswagen's sustainability strategy?"

docs = retrieve_documents(db, query)

for i, doc in enumerate(docs):

    print("=" * 80)
    print(f"Result {i+1}")
    print("=" * 80)

    print(doc.page_content)

    print()