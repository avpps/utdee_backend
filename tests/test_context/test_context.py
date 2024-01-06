import unittest

from utdee_backend.context import Context
from tests.utils import ContextMock


class TestContext(ContextMock, unittest.TestCase):

    def test_context(self):
        context = Context()
        setattr(context, "test", "value")
        context = Context()
        self.assertEqual(getattr(context, "test"), "value")

    def test_context_separation(self):
        context = Context()
        with self.assertRaises(AttributeError):
            getattr(context, "test")
