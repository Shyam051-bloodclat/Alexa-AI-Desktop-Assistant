# Alexa AI Desktop Assistant

A Python-based AI-powered desktop voice assistant that combines speech recognition, text-to-speech, Generative AI, web automation, and Windows desktop automation.

This project was built as a practical learning project to understand how different Python modules, APIs, and automation tools can work together to create a real-world AI application.

## Features

- Voice interaction using Speech Recognition
- Wake-word detection using "Alexa"
- Natural voice responses using Edge TTS
- Gemini AI integration for general questions
- Open Windows applications such as:
  - Google Chrome
  - Notepad
  - Calculator
  - Paint
- Google search
- YouTube playback
- Website opening
- Wikipedia information retrieval
- Battery status
- Current date and time
- Joke generation
- Screenshot functionality
- Modular Python project structure
- API key protection using environment variables
- Git and GitHub version control

## Project Architecture

The project is divided into separate modules so that each part of the assistant has a specific responsibility.

```text
Alexa AI Desktop Assistant
│
├── main.py
├── speech.py
├── commands.py
├── apps.py
├── web.py
├── utilities.py
├── ai.py
├── test.py
├── .gitignore
└── README.md