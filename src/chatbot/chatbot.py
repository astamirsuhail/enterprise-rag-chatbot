from langchain_chroma import Chroma


def load_vector_db(embeddings):

    db = Chroma(
        persist_directory="data/vector_db",
        embedding_function=embeddings
    )

    return db


def retrieve_documents(db, question, top_k=5):

    results = db.similarity_search_with_relevance_scores(
        question,
        k=top_k
    )

    docs = []
    debug_results = []

    for i, (doc, score) in enumerate(results, start=1):

        source = doc.metadata.get("source", "Unknown")

        debug_results.append({
            "rank": i,
            "score": round(score, 4),
            "source": source,
            "content": doc.page_content[:500]
        })

        # Temporary threshold
        if score >= 0.35:
            doc.metadata["relevance_score"] = score
            docs.append(doc)

    return docs, debug_results