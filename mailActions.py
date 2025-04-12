import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

def sendIdea(messageText, messageContact):
    # Load environment variables
    load_dotenv()

    # Credentials und Serverinfos aus .env
    EMAIL_ADDRESS = os.getenv("IDEA_EMAIL")
    EMAIL_PASSWORD = os.getenv("IDEA_PW")
    SMTP_SERVER = os.getenv("Ausgangsserver")
    SMTP_PORT = 465  # SSL-Port

    # Nachricht erstellen
    msg = EmailMessage()
    msg['Subject'] = f'Neue Idee von: {messageContact}'
    msg.set_content(messageText)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    try:
        # Verbindung mit SSL direkt herstellen
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ E-Mail erfolgreich über SiteGround gesendet!")
    except Exception as e:
        print(f"❌ Fehler beim Senden: {e}")
