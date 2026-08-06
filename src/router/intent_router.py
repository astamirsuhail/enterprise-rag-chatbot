def detect_intent(question):

    q = question.lower()

    if any(word in q for word in [
        "travel",
        "trip",
        "flight"
    ]):
        return "TRAVEL"

    elif any(word in q for word in [
        "visa",
        "passport",
        "permit"
    ]):
        return "VISA"

    elif any(word in q for word in [
        "hotel",
        "stay",
        "accommodation"
    ]):
        return "HOTEL"

    elif any(word in q for word in [
        "forex",
        "currency"
    ]):
        return "FOREX"

    elif any(word in q for word in [
        "leave",
        "holiday",
        "vacation"
    ]):
        return "HR"

    return "GENERAL"