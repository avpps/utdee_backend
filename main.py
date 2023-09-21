import os

from bottle import Bottle, run
from pymongo import MongoClient
from pendulum import now


PORT = int(os.getenv("PORT"))

MONGO_URI = os.getenv("MONGO_URI")
MONGO_TEST_DB = os.getenv("MONGO_TEST_DB")
MONGO_TEST_USER = os.getenv("MONGO_TEST_USER")
MONGO_TEST_USER_PASSWORD = os.getenv("MONGO_TEST_USER_PASSWORD")
GUNICORN_CERT = os.getenv("GUNICORN_CERT")
GUNICORN_KEY = os.getenv("GUNICORN_KEY")


backend = Bottle()


@backend.route('/entry')
def entry():
    with open(MONGO_TEST_USER_PASSWORD) as f:
        password = f.read()

    mongo_client = MongoClient(
        f"{MONGO_URI}/{MONGO_TEST_DB}",
        username=MONGO_TEST_USER, password=password,
    )

    test_db = mongo_client[MONGO_TEST_DB]
    _entry = {f"sample_{now()}": "test"}
    inserted_id = test_db["entries"].insert_one(_entry).inserted_id
    return " | ".join((str(len(list(test_db["entries"].find()))), str(inserted_id)))


if __name__ == '__main__':
    run(
        app=backend,
        host="0.0.0.0",
        port=PORT,
        debug=True,
        server="gunicorn",
        keyfile=GUNICORN_KEY,
        certfile=GUNICORN_CERT,
    )
