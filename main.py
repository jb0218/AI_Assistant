from core.engine import speak, wish_me
from core.listener import take_command
from core.commands import execute_command

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if query:
            if "shutdown" in query:
                speak("Shutting down. Goodbye!")
                break
            execute_command(query)