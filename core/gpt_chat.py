import openai
from core.engine import speak
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def chat_with_gpt(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        reply = response['choices'][0]['message']['content']
        speak(reply)
    except:
        speak("I couldn't connect to GPT.")