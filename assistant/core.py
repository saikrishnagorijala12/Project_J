from assistant.config import tts, intents,nlp,recognizer,WAKE_WORDS,p
import speech_recognition as sr



# ------------------ Speak Function ------------------
def speak(text):
    print(f"Jarvis: {text}")
    tts.say(text)
    tts.runAndWait()

# ------------------ Listen Function ------------------
def listen(timeout=None, phrase_time_limit=None):
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        if timeout:
            print(f"Listening for {timeout} seconds...")
        else:
            print("Listening...")

        try:
            # For short inputs, use phrase_time_limit to capture quick speech
            if phrase_time_limit is None:
                phrase_time_limit = 3  # Allow up to 3 seconds of speech
            audio = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
            )
            result = recognizer.recognize_google(audio).lower()
            print(f"Raw recognition result: '{result}'")  # Debug line
            return result

        except sr.UnknownValueError:
            print("Speech was unclear")
            return ""
        except sr.RequestError as e:
            speak(f"Speech service error: {e}")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timeout - no speech detected")
            return ""


# ------------------ Specialized Number Listening Function ------------------
def listen_for_number(timeout=15, max_attempts=3):
    """Specialized function for listening to numbers with better sensitivity"""

    for attempt in range(max_attempts):
        with sr.Microphone() as source:
            # More aggressive noise adjustment for short sounds
            print(f"Adjusting for ambient noise (attempt {attempt + 1})...")
            recognizer.adjust_for_ambient_noise(source, duration=1.0)

            # Lower energy threshold for short sounds
            recognizer.energy_threshold = 300  # Lower threshold
            recognizer.dynamic_energy_threshold = True
            recognizer.pause_threshold = 0.5  # Shorter pause detection

            print(f"Listening for numbers (attempt {attempt + 1}/{max_attempts})...")

            try:
                # Listen with shorter phrase limit for single digits
                audio = recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=2,  # Shorter limit for single digits
                )

                result = recognizer.recognize_google(audio).lower()
                print(f"Attempt {attempt + 1} - Heard: '{result}'")

                if result.strip():  # If we got something
                    return result

            except sr.UnknownValueError:
                print(f"Attempt {attempt + 1} - Speech unclear")
            except sr.RequestError as e:
                print(f"Attempt {attempt + 1} - Service error: {e}")
            except sr.WaitTimeoutError:
                print(f"Attempt {attempt + 1} - Timeout")

        if attempt < max_attempts - 1:
            speak("I didn't catch that. Please speak a bit louder and clearer.")

    return ""

# ------------------ Preprocess ------------------
def preprocess(text):
    doc = nlp(text.lower())
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

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

# ------------------ Main AI Function ------------------
def ask_ai(prompt):
    intent = classify_intent(prompt)
    from assistant.intents_handler import handle_intent

    return handle_intent(intent, prompt)

# ------------------ Wake Word Listener ------------------
def listen_for_wake_word():
    while True:
        text = listen(timeout=3)
        if any(w in text for w in WAKE_WORDS):
            speak("Yes, I am listening. What can I do for you?")
            return True

# ------------------ Enhanced Number Parser ------------------
def parse_number(text):
    """Convert spoken numbers to integers with comprehensive parsing"""
    if not text:
        return None

    # Clean the input
    text = text.lower().strip()

    # Remove common time-related words
    time_words = ["minutes", "minute", "mins", "min", "from", "now", "in", "after"]
    for word in time_words:
        text = text.replace(word, "").strip()

    # Try direct conversion first (for digits like "5", "15", "22")
    try:
        return int(text)
    except ValueError:
        pass

    # Comprehensive word-to-number dictionary
    word_to_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "twenty-one": 21,
        "twenty-two": 22,
        "twenty-three": 23,
        "twenty-four": 24,
        "twenty-five": 25,
        "twenty-six": 26,
        "twenty-seven": 27,
        "twenty-eight": 28,
        "twenty-nine": 29,
        "thirty": 30,
        "thirty-five": 35,
        "forty": 40,
        "forty-five": 45,
        "fifty": 50,
        "fifty-five": 55,
        "sixty": 60,
    }

    # Check for direct word match
    if text in word_to_num:
        return word_to_num[text]

    # Handle compound numbers like "twenty five" (with space)
    text_no_space = text.replace(" ", "-")
    if text_no_space in word_to_num:
        return word_to_num[text_no_space]

    # Handle cases like "2 5" being interpreted as "25"
    if " " in text:
        digits = text.split()
        if len(digits) == 2 and all(d.isdigit() for d in digits):
            return int("".join(digits))

    # Handle repeated words like "one one" = 11
    words = text.split()
    if len(words) == 2 and words[0] == words[1] and words[0] in word_to_num:
        digit = str(word_to_num[words[0]])
        return int(digit + digit)  # "one one" becomes 11

    # Handle cases where there might be extra words but a single number exists
    words = text.split()
    for word in words:
        try:
            return int(word)
        except ValueError:
            if word in word_to_num:
                return word_to_num[word]

    # Try using inflect library for more complex number parsing
    try:
        # Handle written numbers like "twenty-five", "thirty-seven"
        for num in range(1, 100):
            if (
                p.number_to_words(num).replace("-", " ") == text
                or p.number_to_words(num) == text
            ):
                return num
    except:
        pass

    return None