WORKFLOWS = {

    "VISA":[
        "Manager Approval",
        "Invitation Letter",
        "Passport Submission",
        "Visa Processing",
        "Travel Booking"
    ],

    "TRAVEL":[
        "Manager Approval",
        "Travel Request",
        "Flight Booking",
        "Hotel Booking",
        "Expense Claim"
    ],

    "FOREX":[
        "Travel Approval",
        "Forex Request",
        "Receive Forex Card",
        "Expense Settlement"
    ],

    "HR":[
        "Employee Request",
        "Manager Approval",
        "HR Review",
        "Completion"
    ]

}


def get_workflow(intent):

    return WORKFLOWS.get(intent)