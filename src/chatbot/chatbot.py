from langchain_chroma import Chroma


def load_vector_db(embeddings):

    db = Chroma(
        persist_directory="data/vector_db",
        embedding_function=embeddings
    )

    return db


def retrieve_documents(db, question, top_k=5):

    docs = db.similarity_search(
        question,
        k=top_k
    )

    print("=" * 60)
    print("QUESTION:", question)
    print("Retrieved:", len(docs))

    for i, doc in enumerate(docs, start=1):
        print(f"\nChunk {i}")
        print("SOURCE:", doc.metadata.get("source", "Unknown"))
        print(doc.page_content[:300])

    print("=" * 60)

    return docs