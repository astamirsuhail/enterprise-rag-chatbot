from langchain_chroma import Chroma


def create_vector_store(chunks, embeddings):

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="data/vector_db"
    )

    print("Vector database created successfully.")

    return vector_db