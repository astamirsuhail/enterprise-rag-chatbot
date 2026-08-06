def get_recommendations(question):

    q = question.lower()

    # Business Travel
    if "travel" in q:
        return [
            "Hotel Booking Policy",
            "Forex Policy",
            "Visa Policy",
            "Expense Claim"
        ]

    # Hotel
    elif "hotel" in q:
        return [
            "Business Travel Policy",
            "Forex Policy",
            "Expense Claim",
            "Visitor Management"
        ]

    # Visa
    elif "visa" in q or "passport" in q:
        return [
            "Business Travel Policy",
            "Required Documents",
            "Forex Policy",
            "Hotel Booking Policy"
        ]

    # Forex / Expenses
    elif "forex" in q or "expense" in q or "claim" in q:
        return [
            "Business Travel Policy",
            "Hotel Booking Policy",
            "Visa Policy",
            "Procurement SOP"
        ]

    # Leave
    elif "leave" in q:
        return [
            "HR Policies",
            "Work From Home Policy",
            "Holiday Calendar",
            "Employee Attendance"
        ]

    # Work From Home
    elif "work from home" in q or "wfh" in q:
        return [
            "Leave Policy",
            "HR Policies",
            "Information Security",
            "Visitor Management"
        ]

    # Procurement
    elif "procurement" in q or "purchase" in q or "vendor" in q:
        return [
            "Approval Matrix",
            "Purchase Process",
            "Expense Policy",
            "Information Security"
        ]

    # Security
    elif "security" in q or "password" in q or "information" in q:
        return [
            "Visitor Management",
            "Information Security",
            "Work From Home Policy",
            "HR Policies"
        ]

    # Visitor
    elif "visitor" in q:
        return [
            "Information Security",
            "Facility SOP",
            "Reception Process",
            "Security Policy"
        ]

    # Facility
    elif "facility" in q:
        return [
            "Visitor Management",
            "Information Security",
            "Business Travel Policy",
            "HR Policies"
        ]

    # Default
    else:
        return [
            "Business Travel Policy",
            "Hotel Booking Policy",
            "Leave Policy",
            "Information Security"
        ]