# Jarvis - Voice AI Assistant

Jarvis is a simple **voice-enabled AI assistant** built with Python.  
It can listen for a **wake word**, process natural language, perform system tasks, search the web, fetch weather, set reminders, and more.  

---

## 🚀 Features
- 🎙️ **Wake word detection** ("Jarvis")  
- 🗣️ **Speech-to-text & Text-to-speech** interaction  
- 🔍 **DuckDuckGo-powered web search** with summarization  
- 🌦️ **Weather lookup** (via API integration)  
- ⏰ **Reminder system** (voice-based reminders)  
- 💻 **System commands** (open apps, shutdown, restart, etc.)  
- 👋 **Greeting a friend by name** (name extracted from voice input)  

---

## 📂 Project Structure
project/
│── jarvis/
│ ├── init.py
│ ├── main.py # Main entry point
│ ├── intents.py # Intent classification & keywords
│ ├── handlers/
│ │ ├── init.py
│ │ ├── search.py # Web search (DuckDuckGo API)
│ │ ├── weather.py # Weather handler
│ │ ├── reminder.py # Reminder handler
│ │ ├── system.py # System command handler
│ │ └── greeting.py # Greeting handler
│ ├── nlp.py # spaCy preprocessing & intent detection
│ ├── speech.py # Speech recognition & TTS
│ └── utils.py # Helper functions (summarizer, etc.)
│
├── README.md
├── requirements.txt
└── run.sh # (Optional) Shell script to run Jarvis


---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/jarvis-assistant.git
   cd jarvis-assistant


Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Download spaCy model

python -m spacy download en_core_web_sm

▶️ Running Jarvis

Run the assistant:

python -m jarvis.main


Jarvis will:

Wait for the wake word ("Jarvis")

Listen for commands

Respond with voice + text

🧩 Example Commands

Greeting

"Jarvis, say hi to John"

Web Search

"Jarvis, search for the latest iPhone"

Weather

"Jarvis, what's the weather in London?"

Time

"Jarvis, what time is it?"

Reminder

"Jarvis, remind me to call mom at 7 PM"

System Command

"Jarvis, open Chrome"

"Jarvis, shutdown the system"

📦 Requirements

Python 3.8+

speechrecognition

pyttsx3

spacy

duckduckgo-search

(Optional) Weather API key (OpenWeatherMap, etc.)

Install all at once:

pip install -r requirements.txt

🛠️ Future Enhancements

🔑 Integration with Perplexity or Gemini for richer answers

📅 Persistent calendar & reminders

🖥️ GUI interface

🤖 Smarter NLP intent classification

📜 License

MIT License © 2025 [Sai Krishna Gorijala]
