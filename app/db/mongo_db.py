from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

CONNECTION_STRING = "mongodb://testcase1_db:27017"


def init_database():
    client = MongoClient(CONNECTION_STRING)

    try:
        client.admin.command('ping')
    except ConnectionFailure:
        print("Server not available")

    return client['wallet_balances']


db = init_database()
db_crv_current = db["crv_current"]
db_crv_history = db["crv_history"]
