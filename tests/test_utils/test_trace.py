import unittest

from sources.utils.trace import otel_trace
from tests.utils import context_mock_setup


class TestOtelTrace(unittest.TestCase):

    def setUp(self):
        self.context = context_mock_setup()

    def test_otel_trace(self):

        @otel_trace
        def func():
            pass

        for i in range(1, 5):
            with self.subTest(func()):
                self.assertEqual(self.context.tracer.start_as_current_span.call_count, i)
