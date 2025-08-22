from core.speak import speak
from core.intents import intents
from config import nlp
from modules.jokes import handle_jokes
from modules.remider import set_reminder
from modules.greet_friend import handle_greet_friend
from modules.weather import get_weather,ask_city
from modules.system import handle_system
from modules.file import handle_file
from modules.wikipedia import handle_wikipedia
from modules.google import handle_search
import datetime

# ------------------ Intent Handlers ------------------
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
    elif intent == "joke":
        return handle_jokes()
    else:
        return "Hmm, I didn't understand that. Could you rephrase?"


# ------------------ Intent Classifier ------------------
def classify_intent(text):
    tokens = preprocess(text)
    greeting_words = intents.get("greeting", [])


    if any(word in tokens for word in greeting_words):
        doc = nlp(text)
        if any(ent.label_ == "PERSON" for ent in doc.ents):
            return "greet_friend"
        return "greeting"


    for intent, keywords in intents.items():
        if any(word in tokens for word in keywords):
            return intent
    return "unknown"

# ------------------ Preprocess ------------------
def preprocess(text):
    doc = nlp(text.lower())
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

# ------------------ Main AI Function ------------------
def ask_ai(prompt):
    intent = classify_intent(prompt)
    return handle_intent(intent, prompt)