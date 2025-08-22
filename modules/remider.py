from config import reminders
from core.speak import speak
from core.listen import listen
import datetime


# ------------------ Reminders Lookup ------------------
def set_reminder():
    speak("What should I remind you about?")
    task = listen(timeout=10)
    if not task:
        speak("I didn't catch that. Please try again later.")
        return "Reminder not set."

    speak("When should I remind you? Please say in minutes from now.")
    time_input = listen(timeout=10)

    try:
        minutes = int(time_input)
        remind_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
        reminders.append((remind_time, task))
        return f"Reminder set for {minutes} minutes from now: {task}"
    except ValueError:
        return "Could not understand the time. Reminder not set."

def check_reminders():
    now = datetime.datetime.now()
    for r in reminders[:]:
        remind_time, task = r
        if now >= remind_time:
            speak(f"Reminder: {task}")
            reminders.remove(r)