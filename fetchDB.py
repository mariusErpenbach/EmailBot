from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    myDB = client["erpnetDB"]
    myCollections = myDB["ideas"]
    myList = list(myCollections.find())
    counterEntry = myList[0]
    lastSeen= counterEntry["counter"] # Wieviele Einträge waren letztes mal
    newIdeas = len(myList) - lastSeen

    print("last time where",lastSeen,"")

    print(newIdeas)


    myList.reverse()
    for i in range(newIdeas):
            print(myList[i])

    # myList[0].update_one(
    #     {"id_":myList[0]["_id"]},
    #     {"$set":{"counter": len(myList)}}
    # )





except Exception as e:
    print(e)