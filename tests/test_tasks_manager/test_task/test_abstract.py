import unittest

from sources.tasks_manager.task.abstract import AbstractTask


class TestAbstract(unittest.TestCase):

    def test_abstract_instance(self):
        with self.assertRaises(TypeError):
            AbstractTask()

    def test_instance(self):
        class Task(AbstractTask):
            def run(self):
                pass

        self.assertTrue(isinstance(Task(), AbstractTask))
