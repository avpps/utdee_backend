import unittest

from utdee_backend.utils.trace import otel_trace
from tests.utils import ContextMock


class TestOtelTrace(ContextMock, unittest.TestCase):

    def test_otel_trace(self):

        @otel_trace
        def func():
            pass

        for i in range(1, 5):
            with self.subTest(func()):
                self.assertEqual(self.context.tracer.start_as_current_span.call_count, i)
