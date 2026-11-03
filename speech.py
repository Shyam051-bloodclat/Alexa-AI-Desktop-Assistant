import asyncio
import os
import tempfile

import edge_tts
import speech_recognition as sr
from playsound import playsound

# ---------------------------
# SETTINGS
# ---------------------------

VOICE = "en-US-AriaNeural"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300


# ---------------------------
# TEXT TO SPEECH
# ---------------------------

async def _tts(text, filename):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )
    await communicate.save(filename)


def speak(text):

    print(f"Alexa: {text}")

    filename = os.path.join(
        tempfile.gettempdir(),
        "alexa.mp3"
    )

    asyncio.run(_tts(str(text), filename))

    if os.path.exists(filename):
        playsound(filename)
        os.remove(filename)


# ---------------------------
# SPEECH TO TEXT
# ---------------------------

def listen():

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        recognizer.pause_threshold = 1.5

        print("\nListening...")

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:
            return ""

    try:

        text = recognizer.recognize_google(audio).lower()

        print(f"You: {text}")

        return text

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        print("No Internet Connection")
        return ""