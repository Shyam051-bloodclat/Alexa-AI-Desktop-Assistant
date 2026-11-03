import webbrowser
import wikipedia
import pywhatkit


SPECIAL_SITES = {

    "gmail": "https://mail.google.com",

    "chatgpt": "https://chatgpt.com",

    "maps": "https://maps.google.com",
}


def google(query):

    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )


def youtube(song):

    pywhatkit.playonyt(song)


def wiki(person):

    try:

        return wikipedia.summary(
            person,
            sentences=2
        )

    except wikipedia.DisambiguationError:

        return "Please be more specific."

    except wikipedia.PageError:

        return "I couldn't find information."

    except Exception:

        return "Wikipedia is unavailable."


def open_website(name):

    name = name.lower().strip()

    if name in SPECIAL_SITES:

        webbrowser.open(SPECIAL_SITES[name])

    else:

        webbrowser.open(
            f"https://www.{name}.com"
        )

    return True