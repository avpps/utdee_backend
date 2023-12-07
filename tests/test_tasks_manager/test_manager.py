import unittest

from sources.tasks_manager import TasksManager
from sources.tasks_manager.manager import AbstractTasksManager


class TestAbstractTasksManager(unittest.TestCase):

    def test_abstract_instance(self):
        with self.assertRaises(TypeError):
            AbstractTasksManager()


class TestTasksManager(unittest.TestCase):

    @unittest.SkipTest
    def test_instance(self):
        instance = TasksManager()
