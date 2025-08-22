import speech_recognition as sr
from config import recognizer,WAKE_WORDS
from core.speak import speak

# ------------------ Listen Function ------------------
def listen(timeout=None):
    with sr.Microphone() as source:
        if timeout:
            print(f"Listening for {timeout} seconds...")
        else:
            print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout)
            # print("KeyWord : "+recognizer.recognize_google(audio).lower())
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Speech service unavailable.")
            return ""
        except sr.WaitTimeoutError:
            return ""


# ------------------ Wake Word Listener ------------------
def listen_for_wake_word():
    while True:
        text = listen(timeout=3)
        if any(w in text for w in WAKE_WORDS):
            speak("Yes, I am listening. What can I do for you?")
            return True

