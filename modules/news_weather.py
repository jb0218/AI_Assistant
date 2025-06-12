import requests
from core.engine import speak

def daily_briefing():
    speak("Here's your news and weather update.")
    try:
        news = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=your_newsapi_key").json()
        headlines = [article['title'] for article in news['articles'][:3]]
        for h in headlines:
            speak(h)
    except:
        speak("Couldn't fetch the news right now.")