import unittest
from unittest.mock import Mock

from sources.tasks_manager.factory import ListOfTasksFactory
from sources.tasks_manager.task.abstract import AbstractTask
from sources.tasks_manager.dispather.abstract import AbstractTasksDispatcher


class TestListOfTasksFactory(unittest.TestCase):

    def setUp(self):
        self.tasks_number = 5
        self.list_of_tasks = [Mock(spec=AbstractTask) for i in range(self.tasks_number)]
        self.dispatcher = Mock(spec=AbstractTasksDispatcher)

    def test_instance(self):
        ListOfTasksFactory(self.list_of_tasks)

    def test_tasks_manager(self):
        factory = ListOfTasksFactory(self.list_of_tasks)
        factory.dispatcher = self.dispatcher
        factory.start()

        self.assertEqual(self.dispatcher.run_task.call_count, self.tasks_number)
        self.assertListEqual(
            [next(iter(c.kwargs.values())) for c in self.dispatcher.run_task.call_args_list],
            self.list_of_tasks
        )
