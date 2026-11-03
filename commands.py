from speech import speak
from utilities import *
from apps import *
from web import *
from ai import ask_ai
from web import open_website


def execute(text):

    text = text.lower().strip()

    if "time" in text:
        speak(current_time())

    elif "date" in text:
        speak(current_date())

    elif "battery" in text:
        speak(f"Battery is {battery()} percent")

    elif "joke" in text:
        speak(joke())

    elif "screenshot" in text:
        screenshot()
        speak("Screenshot saved.")

    elif "open calculator" in text:
        open_calculator()
        speak("Opening Calculator")

    elif "open paint" in text:
        open_paint()
        speak("Opening Paint")

    elif "open notepad" in text:
        open_notepad()
        speak("Opening Notepad")

    elif "open chrome" in text:
        try:
            open_chrome()
            speak("Opening Chrome")
        except Exception:
            speak("Unable to open Chrome.")

    elif text.startswith("play"):
        song = text.replace("play", "", 1).strip()
        youtube(song)
        speak(f"Playing {song}")

    elif text.startswith("search"):
        query = text.replace("search", "", 1).strip()
        google(query)
        speak(f"Searching {query}")

    elif text.startswith("who is"):
        person = text.replace("who is", "", 1).strip()
        speak(wiki(person))

    elif text.startswith("open"):
        website = text.replace("open", "", 1).strip()

        if website:
            open_website(website)
            speak(f"Opening {website}")
        else:
            speak("Which website should I open?")

    else:
        try:
            speak(ask_ai(text))
        except Exception:
            speak("Sorry, I couldn't connect to AI.")