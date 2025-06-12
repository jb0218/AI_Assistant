import smtplib
from core.engine import speak

def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('youremail@gmail.com', 'yourpassword')
        server.sendmail('youremail@gmail.com', 'toemail@gmail.com', 'Test email from Jarvis')
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email: {e}")