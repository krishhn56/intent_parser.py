# Nexa Execution Layer - Intent Parser Prototype

def parse_intent(command):
    if "open" in command:
        return "OPEN_APP"
    elif "search" in command:
        return "SEARCH_WEB"
    elif "run" in command:
        return "EXECUTE_TASK"
    else:
        return "UNKNOWN"
