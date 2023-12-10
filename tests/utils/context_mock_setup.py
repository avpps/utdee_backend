import unittest.mock
from opentelemetry.trace import Tracer
from sources.context import Context


class ContextMock:

    @unittest.mock.patch.dict("sources.context.settings.os.environ", {
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
