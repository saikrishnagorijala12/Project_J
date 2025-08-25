import inflect
import pyttsx3
import spacy
import speech_recognition as sr

# ------------------ Initialize ------------------
nlp =   spacy.load("en_core_web_sm")
recognizer = sr.Recognizer()
tts = pyttsx3.init()
tts.setProperty('rate', 160)
tts.setProperty('volume', 1.0)
p = inflect.engine()
WAKE_WORDS = ["jarvis", "hey jarvis"]
reminders = []
number_to_guess = None
current_mood = "serious"

# ------------------ Intents ------------------
intents = {
    "greeting": ["hello", "hi", "hey", "morning"],
    "exit": ["bye", "quit", "exit"],
    "greet_friend" :['friend'],
    "weather": ["weather", "forecast", "temperature"],
    "time": ["time", "clock"],
    "date": ["date", "day", "today"],
    "system_command": ["open", "launch", "run", "shutdown", "restart", "volume", "brightness", "ip"],
    "file": ["file", "folder", "directory", "create", "delete", "list"],
    "wikipedia": ["wikipedia", "who", "what", "tell me about"],
    "search": ["search", "google", "look up", "find"],
    "fun": ["joke", "fun", "trivia", "question"],
    "game": ["play", "game", "number guess", "tic tac toe"],
    "mood": ["serious", "funny", "sarcastic", "mood"],
    "sleep": ["sleep", "standby"],
    "reminder" : ["remind", "reminder", "note"],
}