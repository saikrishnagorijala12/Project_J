from core.speak import speak
from core.listen import listen
import requests


# ------------------ Weather Friend ------------------
def ask_city():
    speak("Which city would you like the weather for?")
    city = listen(timeout=5)
    if not city:
        speak("I didn't catch that. Using default city Guntur.")
        city = "Guntur"
    return city

def get_weather(city):
    api_key = "431a1f97c7bb066efa54bbc925a4a715"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        res = requests.get(url, timeout=5).json()
        if res.get("cod") != 200:
            return f"Could not get weather for {city}."
        desc = res['weather'][0]['description']
        temp = res['main']['temp']
        feels = res['main']['feels_like']
        humidity = res['main']['humidity']
        return f"Weather in {city}: {desc}, temperature {temp}°C, feels like {feels}°C, humidity {humidity}%."
    except Exception as e:
        return f"Error fetching weather: {e}"