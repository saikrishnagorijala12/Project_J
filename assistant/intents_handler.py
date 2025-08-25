# ------------------ Intent Handlers ------------------
import datetime
from assistant.core import speak,intents
from assistant.modules.Wikipedia import handle_wikipedia
from assistant.modules.file import handle_file
from assistant.modules.fun import handle_fun
from assistant.modules.game import handle_game
from assistant.modules.greet import handle_greet_friend
from assistant.modules.personality import respond_with_mood, set_mood
from assistant.modules.reminder import set_reminder
from assistant.modules.search import handle_search
from assistant.modules.system import handle_system
from assistant.modules.weather import get_weather, ask_city



def handle_sleep(intent):
    if intent in ["sleep", "standby"]:
        speak("Going back to standby. Say 'Jarvis' to wake me up again.")


def handle_intent(intent, text, ):
    if intent == "greeting":
        return "Hello! How can I help you?"
    elif intent == "exit":
        return "Goodbye!"
    elif intent == "sleep":
        return "Sleep Mode"
    elif intent == "greet_friend":
        return handle_greet_friend(text)
    elif intent == "weather":
        city = ask_city()
        return get_weather(city)
    elif intent == "time":
        return f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif intent == "date":
        return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"
    elif intent == "system_command":
        return handle_system(text)
    elif intent == "file":
        return handle_file(text)
    elif intent == "wikipedia":
        return handle_wikipedia(text)
    elif intent == "reminder":
        return set_reminder()
    elif intent == "search":
        return handle_search(text)
    elif intent == "fun":
        return respond_with_mood(handle_fun(text))
    elif intent == "game":
        return respond_with_mood(handle_game(text))
    elif intent == "mood":
        mood = text.lower()
        if "funny" in mood:
            return set_mood("funny")
        elif "sarcastic" in mood:
            return set_mood("sarcastic")
        else:
            return set_mood("serious")
    else:
        return "Hmm, I didn't understand that. Could you rephrase?"
