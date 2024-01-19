from bottle import run

from utdee_backend.utils.trace import setup_otel_tracer
from utdee_backend.context import Context
from utdee_backend.db.mysql import db_engine, db_session_class

from utdee_backend.api import *


if __name__ == '__main__':
    context = Context()
    context.tracer = setup_otel_tracer()
    context.db_session_class = db_session_class(db_engine())

    with context.db_session_class() as db_session:
        context.db_session = db_session

        run(
            host="0.0.0.0",
            port=context.settings.PORT,
            debug=True,
            server="gunicorn",
            keyfile=context.settings.GUNICORN_KEY,
            certfile=context.settings.GUNICORN_CERT,
        )
