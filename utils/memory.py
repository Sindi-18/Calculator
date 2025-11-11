
import os


def update_history(operations: str):
    """Replace operation word with symbols and saves them to a history file."""
    symbols = {
        "add": "+",
        "sub": "-",
        "multiply": "*",
        "divide": "÷",
        "modulo": "%"
    }

    # Replace operation words with their symbols
    for word, symbol in symbols.items():
        operations = operations.replace(word, symbol)

    # Append the processed operation to the history file
    with open("./utils/history", "a") as file:
        file.write(operations + "\n")


def display_history():
    """Displays all saved calculator operations from the history file."""
    try:
        with open("./utils/history") as file:
            lines = file.readlines()

        if not lines:
            return "History is empty."
        else:
            for i, line in enumerate(lines, start=1):
                return f"{i} | {line.strip()}"

    except FileNotFoundError:
        return "No history found."


def delete_history():
    """Deletes the history file and creates a new empty one."""
    try:
        os.remove("./utils/history")  # Remove the old history file
    except FileNotFoundError:
        return FileNotFoundError
        # If it doesn’t exist, just ignore the error

    # Create a new empty file for future history
    with open("./utils/history", "x") as f:
        pass

    return "History cleared."
