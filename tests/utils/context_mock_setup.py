import unittest.mock
from opentelemetry.trace import Tracer
from sources.context import Context


class ContextMock:

    def setUp(self):
        context = Context()
        context.tracer = unittest.mock.create_autospec(Tracer, spec_set=True)

    def tearDown(self):
        Context.clear()

    @property
    def context(self):
        return Context()
