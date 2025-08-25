import random
from assistant.config import number_to_guess

# ------------------ Game Lookup ------------------
def handle_game(text):
    global number_to_guess
    text_lower = text.lower()

    if "number guess" in text_lower:
        number_to_guess = random.randint(1, 20)
        return "I’ve thought of a number between 1 and 20. Try to guess it!"

    elif "guess" in text_lower and number_to_guess is not None:
        try:
            guess = int(text_lower.split("guess")[-1].strip())
            if guess == number_to_guess:
                number_to_guess = None
                return "🎉 Correct! You guessed the number."
            elif guess < number_to_guess:
                return "Too low! Try again."
            else:
                return "Too high! Try again."
        except:
            return "Please guess a number like: guess 7"

    return "Game command not recognized."