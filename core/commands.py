import webbrowser, datetime, pywhatkit, pyautogui
from core.engine import speak
from core.gpt_chat import chat_with_gpt
from modules import emailer, face_unlock, voice_auth, news_weather, notes_reminder, smart_home

def execute_command(query):
    if "youtube" in query:
        pywhatkit.playonyt(query.replace("youtube", ""))
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
    elif "time" in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")
    elif "type" in query:
        speak("What should I type?")
        msg = voice_auth.get_input()  # Simulate input
        pyautogui.typewrite(msg)
    elif "send email" in query:
        emailer.send_email()
    elif "unlock with face" in query:
        face_unlock.unlock()
    elif "authenticate voice" in query:
        voice_auth.authenticate()
    elif "news" in query or "weather" in query:
        news_weather.daily_briefing()
    elif "note" in query or "reminder" in query:
        notes_reminder.manage_notes(query)
    elif "turn on light" in query or "turn off light" in query:
        smart_home.control_devices(query)
    else:
        chat_with_gpt(query)