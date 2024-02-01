import unittest.mock

from opentelemetry.trace import Tracer
from utdee_backend.context import Context
from utdee_backend.db.mysql import db_session_class_mock


def settings_environ():
    return {
        "PORT": "8000",
        "ENV_NAME": "local_test",
        "SECRETS_PATH": "",

        "GUNICORN_KEY": "",
        "GUNICORN_CERT": "",

        "MONGO_TEST_USER_PASSWORD": "",
        "MONGO_TEST_USER": "",
        "MONGO_TEST_DB": "",
        "MONGO_URI": "",

        "MYSQL_DB_NAME": "",
        "MYSQL_DIALECT_DRIVER": "",
        "MYSQL_PASSWORD": "",
        "MYSQL_URI": "",
        "MYSQL_USER": "",

        "SPARK_URL": "",
    }


class ContextMock:

    @unittest.mock.patch.dict("utdee_backend.context.settings.os.environ", settings_environ())
    def setUp(self):
        context = Context()
        context.tracer = unittest.mock.create_autospec(Tracer, spec_set=True)

        context.db_session_class = db_session_class_mock()
        context.db_session = context.db_session_class()

    def tearDown(self):
        Context().db_session.close()
        Context.clear()

    @property
    def context(self):
        return Context()
