import unittest.mock
from opentelemetry.trace import Tracer
from utdee_backend.context import Context

from mongomock import patch


class ContextMock:

    @unittest.mock.patch.dict("utdee_backend.context.settings.os.environ", {
        "PORT": "8000",
        "SPARK_URL": "",
        "GUNICORN_KEY": "",
        "GUNICORN_CERT": "",
        "MONGO_TEST_USER_PASSWORD": "",
        "MONGO_TEST_USER": "",
        "MONGO_TEST_DB": "",
        "MONGO_URI": "",
    })
    def setUp(self):
        context = Context()
        context.tracer = unittest.mock.create_autospec(Tracer, spec_set=True)

    def tearDown(self):
        Context.clear()

    @property
    def context(self):
        return Context()
