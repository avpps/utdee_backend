import unittest

from sources.utils.context_manager import ContextManager


class TestContextManager(unittest.TestCase):

    def test_context_manager_instance(self):
        ContextManager()
        type("CustomContextManager", (ContextManager, ), {})()

    def test_context_manager_with(self):
        with ContextManager():
            pass
