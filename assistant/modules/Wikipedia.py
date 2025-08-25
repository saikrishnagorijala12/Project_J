import wikipedia

# ------------------ Wikipedia Lookup ------------------
def handle_wikipedia(text):
    try:
        query = text
        for kw in ["wikipedia", "who", "what", "tell me about"]:
            query = query.replace(kw, "")
        query = query.strip()
        if not query:
            return "What do you want me to search on Wikipedia?"
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "I couldn't find anything on Wikipedia."