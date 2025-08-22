from config import tts


# ------------------ Speak Function ------------------
def speak(text):
    print(f"Jarvis: {text}")
    tts.say(text)
    tts.runAndWait()