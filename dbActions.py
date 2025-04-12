from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

def get_new_ideas():
    load_dotenv()
    uri = os.getenv("MONGO_URI")

    try:
        # Verbindung zur MongoDB
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["erpnetDB"]
        collection = db["ideas"]

        unsent_ideas = collection.find({"ip": {"$exists": True}})
        return list(unsent_ideas)

    except Exception as e:
        print("Fehler beim Zugriff auf MongoDB:", e)
        return []

def mark_idea_as_sent(idea_id):
    load_dotenv()
    uri = os.getenv("MONGO_URI")

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["erpnetDB"]
        collection = db["ideas"]

        collection.update_one(
            {"_id": idea_id},
            {"$unset": {"ip": ""}}
        )

    except Exception as e:
        print("❌ Fehler beim Aktualisieren der Idee:", e)