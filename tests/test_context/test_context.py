import unittest

from sources.context import Context


class TestContext(unittest.TestCase):

    def test_context(self):
        context = Context()
        setattr(context, "test", "value")
        context = Context()
        self.assertEqual(getattr(context, "test"), "value")
