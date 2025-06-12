from core.engine import speak

def control_devices(query):
    if "turn on light" in query:
        speak("Light turned on.")
    elif "turn off light" in query:
        speak("Light turned off.")