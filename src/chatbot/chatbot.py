from langchain_chroma import Chroma


def load_vector_db(embeddings):

    db = Chroma(
        persist_directory="data/vector_db",
        embedding_function=embeddings
    )

    return db


def retrieve_documents(db, question, top_k=5):

    print("=" * 60)
    print("QUESTION:", question)

    results = db.similarity_search_with_relevance_scores(
        question,
        k=top_k
    )

    docs = []

    for i, (doc, score) in enumerate(results, start=1):

        print(f"\nChunk {i}")
        print("Relevance Score:", round(score, 4))
        print("SOURCE:", doc.metadata.get("source", "Unknown"))
        print("CONTENT:", doc.page_content[:300])

        # Temporary threshold for testing
        if score >= 0.20:
            doc.metadata["relevance_score"] = score
            docs.append(doc)

    print("\nAccepted documents:", len(docs))
    print("=" * 60)

    return docs