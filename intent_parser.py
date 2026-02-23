# Nexa Execution Layer - Intent Parser Prototype

def parse_intent(user_input):

    intent = {
        "task": None,
        "steps": []
    }

    if "email" in user_input.lower():
        intent["task"] = "send_email"
        intent["steps"] = [
            "collect recipient",
            "generate message",
            "send email"
        ]

    elif "report" in user_input.lower():
        intent["task"] = "generate_report"
        intent["steps"] = [
            "collect data",
            "organize information",
            "create document"
        ]

    else:
        intent["task"] = "general_task"
        intent["steps"] = [
            "analyze request",
            "plan execution"
        ]

    return intent


if __name__ == "__main__":
    user = input("Enter task: ")
    result = parse_intent(user)

    print("\nParsed Intent:")
    print(result)
