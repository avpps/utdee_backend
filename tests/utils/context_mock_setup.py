import unittest.mock
from opentelemetry.trace import Tracer
from sources.context import Context


def context_mock_setup() -> Context:
    context = Context()
    context.tracer = unittest.mock.create_autospec(Tracer)
    return Context()
