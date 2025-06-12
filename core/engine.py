import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you?")