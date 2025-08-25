# ------------------ Main Loop ------------------
import os
from assistant.core import speak, listen_for_wake_word, listen, ask_ai
from assistant.modules.reminder import check_reminders


def main():
    speak("Jarvis is online. Say 'Jarvis' to wake me up.")
    check_reminders()

    while True:
        if listen_for_wake_word():
            check_reminders()
            while True:
                check_reminders()
                user_input = listen()
                if not user_input:
                    continue

                user_input_lower = user_input.lower()
                if "sleep" in user_input_lower or 'stand by' in user_input_lower:
                    speak("Going back to standby. Say 'Jarvis' to wake me up again.")
                    break


                if user_input_lower in ["exit", "quit", "bye"]:
                    speak("Goodbye!")
                    return

                if user_input.startswith("!"):
                    command = user_input[1:]
                    try:
                        output = os.popen(command).read()
                        speak(output if output else "Command executed.")
                    except Exception as e:
                        speak(f"Error: {e}")
                else:
                    response = ask_ai(user_input)
                    speak(response)