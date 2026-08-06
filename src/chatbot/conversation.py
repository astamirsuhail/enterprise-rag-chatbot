def build_chat_history(messages):

    history = ""

    for message in messages[-6:]:

        history += f"{message['role']}: {message['content']}\n"

    return history