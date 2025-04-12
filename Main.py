import time
from dbActions import get_new_ideas, mark_idea_as_sent
from mailActions import sendIdea
import logging
# Logging konfigurieren

logging.basicConfig(filename='error_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    while True:  # Endlosschleife
        # Holen der ungesendeten Ideen
        ideas = get_new_ideas()

        if not ideas:
            logging.info("✅ Keine neuen Ideen gefunden.")
        else:
            for idea in ideas:
                message = idea.get("idea", "Kein Inhalt")
                contact = idea.get("kontakt", "Unbekannt")

                # E-Mail senden
                sendIdea(message, contact)

                # Idee nach Versand aktualisieren
                mark_idea_as_sent(idea["_id"])
                logging.info(f"✅ Idee von {contact} versendet: {message}")

        logging.info(f"✅ {len(ideas)} Ideen wurden versendet und aktualisiert.")
        # Warten, bevor der nächste Check gemacht wird (z.B. 1 Stunde)
        logging.info("Warten auf neue Ideen... Nächster Durchlauf in 60 Minuten.")
        time.sleep(3600)  # 3600 Sekunden = 1 Stunde




if __name__ == "__main__":
    main()