
# 🧑‍💻 Jarvis Voice Assistant

Jarvis is a **Python-based voice-controlled AI assistant** that can perform a wide range of tasks, such as answering questions, controlling your system, fetching weather, searching the web, telling jokes, and much more.

---

## 🚀 Features
- 🎤 **Voice Interaction** – Wake word detection (`"Jarvis"`, `"Hey Jarvis"`) and speech recognition.
- 🗣️ **Text-to-Speech** – Responds naturally using `pyttsx3`.
- 🌦️ **Weather Updates** – Fetches real-time weather information (via [OpenWeather API](https://openweathermap.org/)).
- 🕒 **Time & Date** – Announces current time and date.
- 💻 **System Commands** – Open apps (Firefox, Chrome, VS Code, Terminal), control volume, check IP/system info, shutdown/restart.
- 📂 **File Operations** – Create, delete, list, and open folders.
- 📖 **Wikipedia Lookup** – Fetches summaries for topics.
- 🔍 **Google Search** – Finds and reads aloud top search results.
- 😂 **Jokes** – Tells programming jokes using `pyjokes`.
- ⏰ **Reminders** – Set voice-based reminders.
- 👋 **Greeting Friends** – Recognizes names and greets personally.

---

## 🛠️ Requirements

Install the dependencies with:

```bash
pip install speechrecognition pyttsx3 spacy wikipedia google requests beautifulsoup4 pyjokes
```

You also need to download the **spaCy English model**:

```bash
python -m spacy download en_core_web_sm
```

**Additional system dependencies:**
- `ffmpeg` (for `speechrecognition`)
- `pyaudio` (microphone access)
- `neofetch` (for system info, optional)
- Linux system commands (`xdg-open`, `pactl`, etc.) – adapt for Windows/Mac if needed.

---

## 🔑 Setup API Keys
For weather updates, get a free API key from [OpenWeather](https://openweathermap.org/api) and replace in the script:

```python
api_key = "YOUR_API_KEY_HERE"
```

---

## ▶️ Usage

Run the assistant with:

```bash
python jarvis.py
```

Jarvis will announce:
```
Jarvis is online. Say 'Jarvis' to wake me up.
```

Then you can say commands like:
- "Jarvis, what’s the weather in London?"
- "Jarvis, open Chrome"
- "Jarvis, tell me a joke"
- "Jarvis, remind me to drink water in 5 minutes"
- "Jarvis, search Python tutorials on Google"

To stop:
- Say **"exit"**, **"quit"**, or **"bye"**.

---

## ⚠️ Notes
- Optimized for **Linux**. You may need to adjust system commands for Windows/Mac.
- Requires a working microphone and speakers.
- Background standby mode until wake word is detected.

---

## 📌 Roadmap
- [ ] Cross-platform system command support (Windows/Mac).
- [ ] Better intent classification (using ML models).
- [ ] Continuous listening mode toggle.
- [ ] GUI interface.

---

## 🤝 Contributing
Contributions are welcome!  
Feel free to fork, open issues, and submit pull requests.

---

## 📜 License
This project is licensed under the MIT License – feel free to use and modify.

---
