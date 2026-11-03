from speech import listen, speak
from commands import execute

WAKE_WORD = "alexa"

speak("Hello! I am your laptop assistant.")

while True:

    text = listen()

    if not text:
        continue

    # Exit anytime
    if "exit" in text or "goodbye" in text:
        speak("Goodbye!")
        break

    # Ignore speech without wake word
    if WAKE_WORD not in text:
        continue

    # Remove wake word
    command = text.replace(WAKE_WORD, "").strip()

    if not command:
        speak("Yes?")
        continue

    print(f"Command: {command}")

    try:
        execute(command)

    except Exception as e:
        print(e)
        speak("Something went wrong.")