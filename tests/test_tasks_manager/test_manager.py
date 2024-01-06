import unittest

from utdee_backend.tasks_manager.manager import TasksManager
from utdee_backend.tasks_manager.manager import AbstractTasksManager


class TestAbstractTasksManager(unittest.TestCase):

    def test_abstract_instance(self):
        with self.assertRaises(TypeError):
            AbstractTasksManager()


class TestTasksManager(unittest.TestCase):

    @unittest.expectedFailure
    def test_instance(self):
        instance = TasksManager()
