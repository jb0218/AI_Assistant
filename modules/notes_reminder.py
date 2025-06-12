import sqlite3
from core.engine import speak

def manage_notes(query):
    conn = sqlite3.connect("data/notes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (content TEXT)")
    if "add" in query:
        c.execute("INSERT INTO notes VALUES (?)", ("A new reminder",))
        conn.commit()
        speak("Note added.")
    elif "show" in query:
        for row in c.execute("SELECT * FROM notes"):
            speak(row[0])
    conn.close()