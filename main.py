import os

from bottle import Bottle, run
from pymongo import MongoClient
from pendulum import now

from sources.api.tasks import thread_pool_list_of_get_call_tasks
from sources.tasks_manager import GetCallTask
from sources.utils.trace import setup_otel_tracer, otel_trace
from sources.context import Context


PORT = int(os.getenv("PORT"))

MONGO_URI = os.getenv("MONGO_URI")
MONGO_TEST_DB = os.getenv("MONGO_TEST_DB")
MONGO_TEST_USER = os.getenv("MONGO_TEST_USER")
MONGO_TEST_USER_PASSWORD = os.getenv("MONGO_TEST_USER_PASSWORD")
GUNICORN_CERT = os.getenv("GUNICORN_CERT")
GUNICORN_KEY = os.getenv("GUNICORN_KEY")


backend = Bottle()


@backend.get("/")
@otel_trace
def main_page():
    list_of_tasks = [GetCallTask(u) for u in (
        "https://www.yr.no/api/v0/locations/2-7531926/forecast",
        "https://www.yr.no/api/v0/locations/2-7531926/celestialeventsmultipledays",
        "https://www.yr.no/api/v0/locations/2-7531926/forecast/currenthour",
    )] * 10
    thread_pool_list_of_get_call_tasks(list_of_tasks=list_of_tasks)
    result = ("\n"*3).join(
        f"{t.url}\n{t.result.text}" for t in list_of_tasks
    )
    return f"<html><pre>{result}</pre></html>"


@backend.route('/entry')
@otel_trace
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
    context = Context()
    context.tracer = setup_otel_tracer()
    run(
        app=backend,
        host="0.0.0.0",
        port=PORT,
        debug=True,
        server="gunicorn",
        keyfile=GUNICORN_KEY,
        certfile=GUNICORN_CERT,
    )
