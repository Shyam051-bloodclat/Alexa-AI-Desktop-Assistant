import psutil
import pyautogui
import pyjokes
from datetime import datetime


def battery():

    return psutil.sensors_battery().percent


def joke():

    return pyjokes.get_joke()


def screenshot():

    img = pyautogui.screenshot()

    img.save("assets/screenshot.png")


def current_time():

    return datetime.now().strftime("%I:%M %p")


def current_date():

    return datetime.now().strftime("%d %B %Y")