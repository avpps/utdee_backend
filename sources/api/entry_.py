from bottle import get
from pymongo import MongoClient
from pendulum import now

from sources.utils.trace import otel_trace
from sources.context import Context


@get('/entry')
@otel_trace
def entry():
    context = Context()
    with open(context.settings.MONGO_TEST_USER_PASSWORD) as f:
        password = f.read()

    mongo_client = MongoClient(
        f"{context.settings.MONGO_URI}/{context.settings.MONGO_TEST_DB}",
        username=context.settings.MONGO_TEST_USER, password=password,
    )

    test_db = mongo_client[context.settings.MONGO_TEST_DB]
    _entry = {f"sample_{now()}": "test"}
    inserted_id = test_db["entries"].insert_one(_entry).inserted_id
    return " | ".join((str(len(list(test_db["entries"].find()))), str(inserted_id)))
