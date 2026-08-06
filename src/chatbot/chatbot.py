from langchain_chroma import Chroma


def load_vector_db(embeddings):

    db = Chroma(
        persist_directory="data/vector_db",
        embedding_function=embeddings
    )

    return db


def retrieve_documents(
    db,
    question,
    top_k=5
):

    docs = db.similarity_search(
    question,
    k=top_k
    )

    print("="*50)
    print("QUESTION:", question)
    print("Retrieved:", len(docs))

    for d in docs:
        print(d.metadata)

    print("="*50)

    return docs