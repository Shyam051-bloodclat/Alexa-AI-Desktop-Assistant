import os
import subprocess

def open_notepad():
    subprocess.Popen("notepad")

def open_calculator():
    subprocess.Popen("calc")

def open_paint():
    subprocess.Popen("mspaint")

def open_chrome():

    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
    ]

    for path in possible_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return True

    return False