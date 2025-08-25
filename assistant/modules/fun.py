import random, requests

# ------------------ Fun Section ------------------
def handle_fun(text):
    text_lower = text.lower()

    # Jokes
    if "joke" in text_lower:
        try:
            res = requests.get("https://v2.jokeapi.dev/joke/Any").json()
            if res["type"] == "single":
                return res["joke"]
            else:
                return res["setup"] + " ... " + res["delivery"]
        except:
            return "Sorry, I couldn’t fetch a joke right now."

    # Trivia
    elif "trivia" in text_lower or "question" in text_lower:
        try:
            res = requests.get("https://opentdb.com/api.php?amount=1&type=multiple").json()
            q = res["results"][0]["question"]
            correct = res["results"][0]["correct_answer"]
            options = res["results"][0]["incorrect_answers"] + [correct]
            random.shuffle(options)
            return f"Trivia: {q}\nOptions: {', '.join(options)}\nAnswer: {correct}"
        except:
            return "Couldn’t fetch trivia."

    else:
        return "Fun command not recognized. Try 'tell me a joke' or 'ask me trivia'."
