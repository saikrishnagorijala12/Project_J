from assistant.config import current_mood

# ------------------ Pesonality Engine ------------------
def set_mood(mood):
    global current_mood
    current_mood = mood
    return f"My personality is now {mood}."

def respond_with_mood(response):
    if current_mood == "serious":
        return response
    elif current_mood == "funny":
        return response + " 😂"
    elif current_mood == "sarcastic":
        return "Oh really? " + response + " 🙄"
    else:
        return response