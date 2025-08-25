import datetime
from assistant.config import reminders
from assistant.core import speak,listen,listen_for_number,parse_number

# ------------------ Reminders Lookup ------------------
def set_reminder():
    """Enhanced reminder function with better number recognition"""
    speak("What should I remind you about?")
    task = listen(timeout=10)
    if not task:
        speak("I didn't catch that. Please try again later.")
        return "Reminder not set."

    speak("When should I remind you? Please say the number of minutes clearly.")
    time_input = listen_for_number()


    print(f"DEBUG: Final time input: '{time_input}'")

    if not time_input:
        speak(
            "I couldn't hear the time after multiple attempts. Please try again later."
        )
        return "Reminder not set."

    minutes = parse_number(time_input)

    if minutes is None or minutes <= 0:
        speak(f"I couldn't understand '{time_input}' as a valid number of minutes.")
        return "Could not understand the time. Reminder not set."

    remind_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    reminders.append((remind_time, task))

    print(f"DEBUG: Set reminder for {minutes} minutes: {task}")
    return f"Reminder set for {minutes} minutes from now: {task}"


def check_reminders():
    now = datetime.datetime.now()
    for r in reminders[:]:
        remind_time, task = r
        if now >= remind_time:
            speak(f"Reminder: {task}")
            reminders.remove(r)