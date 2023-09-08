from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

CONNECTION_STRING = "mongodb://localhost:27017"


def init_database():
    client = MongoClient(CONNECTION_STRING)

    try:
        client.admin.command('ping')
    except ConnectionFailure:
        print("Server not available")

    return client['wallet_balances']


db = init_database()
collection_crv = db["crv"]
