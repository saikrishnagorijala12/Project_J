import requests
from googlesearch import search
import webbrowser
from bs4 import BeautifulSoup
from assistant.core import speak


# ------------------ Google Search (read aloud) ------------------
def summarize_text(text, max_chars=500):
    text = text.replace("\n", " ")
    if len(text) > max_chars:
        return text[:max_chars] + "..."
    return text

def handle_search(text):
    query = text
    for kw in ["search", "google", "look up", "find"]:
        query = query.replace(kw, "")
    query = query.strip()
    if not query:
        return "What should I search for?"

    try:
        results = list(search(query))
        if not results:
            return "I couldn't find anything."

        top_result = results[0]
        speak(f"I found some results for {query}. Reading the top result.")


        webbrowser.open(top_result)


        try:
            r = requests.get(top_result, timeout=5)
            soup = BeautifulSoup(r.text, "html.parser")
            paragraphs = soup.find_all("p")
            text_content = " ".join([p.get_text() for p in paragraphs[:3]])
            summary = summarize_text(text_content)
            if summary:
                speak(summary)
            else:
                speak("No readable text found on this page.")
        except Exception as e:
            speak(f"Couldn't read the page: {e}")

        return f"I read the top result for {query}."
    except Exception as e:
        return f"Error during search: {e}"