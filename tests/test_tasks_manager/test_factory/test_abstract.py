import unittest

from sources.tasks_manager.factory.abstract import AbstractTasksFactory


class TestAbstract(unittest.TestCase):

    def test_abstract_instance(self):
        with self.assertRaises(TypeError):
            AbstractTasksFactory()

    def test_instance(self):
        class TaskFactory(AbstractTasksFactory):
            async def _start(self):
                pass

        self.assertTrue(isinstance(TaskFactory(), AbstractTasksFactory))
