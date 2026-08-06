def classify_query(retrieved_docs):

    """
    Returns:

    COMPANY
    GENERAL
    """

    if len(retrieved_docs) > 0:
        return "COMPANY"

    return "GENERAL"