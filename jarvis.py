import os
import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import pyautogui

# Initialize TTS
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        say("Good Morning!")
    elif hour < 18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")
    say("I am Jarvis. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
        return query.lower()
    except:
        return "none"

def openOnYouTube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    say("Opening YouTube")

def searchOnGoogle(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    say("Searching on Google")

def takeScreenshot():
    if not os.path.exists("Screenshots"):
        os.mkdir("Screenshots")

    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"Screenshots/screenshot_{time}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(path)
    say("Screenshot saved")

# MAIN
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if query == "none":
            continue

        # Open sites
        if "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "open wikipedia" in query:
            webbrowser.open("https://wikipedia.com")
        # Play music
        elif "play music" in query:
            music_dir = "C:\\Musicc"
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                say("Playing music")

        # YouTube search
        elif "on youtube" in query:
            search = query.replace("open", "").replace("on youtube", "")
            openOnYouTube(search)

        # Google search
        elif "on google" in query:
            search = query.replace("search", "").replace("on google", "")
            searchOnGoogle(search)

        # Screenshot
        elif "screenshot" in query:
            takeScreenshot()

        # Time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {time}")

        # Exit
        elif "exit" in query or "quit" in query:
            say("Goodbye")
            break

        else:
            say("I didn't understand that")