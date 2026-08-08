def classify_query(retrieved_docs):

    """
    Classifies the question based on retrieval results.

    Returns:
        COMPANY - relevant company knowledge was found
        GENERAL - no sufficiently relevant company knowledge was found
    """

    if not retrieved_docs:
        return "GENERAL"

    return "COMPANY"