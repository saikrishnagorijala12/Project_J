import spacy
import speech_recognition as sr
import pyttsx3


# ------------------ Initialize ------------------
nlp = spacy.load("en_core_web_sm")
recognizer = sr.Recognizer()
tts = pyttsx3.init()
tts.setProperty('rate', 160)
tts.setProperty('volume', 1.0)
WAKE_WORDS = ["jarvis", "hey jarvis"]
reminders = []