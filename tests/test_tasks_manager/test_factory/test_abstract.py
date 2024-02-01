import unittest

from utdee_backend.tasks_manager.factory.abstract import AbstractTasksFactory


class TestAbstract(unittest.TestCase):

    def test_abstract_instance(self):
        with self.assertRaises(TypeError):
            AbstractTasksFactory()  # noqa

    def test_instance(self):
        class TaskFactory(AbstractTasksFactory):
            async def _start(self):
                pass

        self.assertTrue(isinstance(TaskFactory(), AbstractTasksFactory))
