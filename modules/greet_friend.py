from config import nlp


# ------------------ Greet Friend ------------------
def handle_greet_friend(text):
    doc = nlp(text)

    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    if not names:
        tokens = text.split()
        for i, token in enumerate(tokens):
            if token.lower() == "friend" and i + 1 < len(tokens):
                names.append(tokens[i + 1].capitalize())
                break


    if not names:
        names = [token.text for token in doc if token.text.istitle()]

    if names:
        all_names = ", ".join(names)
        return f"Hey {all_names}! How are you doing today?"
    else:
        return "Hello! Who am I greeting?"