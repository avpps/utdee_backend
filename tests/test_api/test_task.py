import unittest
import unittest.mock as mock

from sources.api import (
    thread_pool_list_of_get_call_tasks,
    process_pool_list_of_get_call_tasks,
)
from sources.tasks_manager import GetCallTask


class TestTasks(unittest.TestCase):

    def setUp(self) -> None:
        self.list_of_get_call_tasks = [
            type("GetCallTask", (GetCallTask, ), {"run": mock.MagicMock()})
            for _ in range(10)
        ]

    def test_thread_pool_tasks(self):
        thread_pool_list_of_get_call_tasks(list_of_tasks=self.list_of_get_call_tasks)
        for result in self.list_of_get_call_tasks:
            result.run.assert_called_once()

    def test_process_pool_tasks(self):
        process_pool_list_of_get_call_tasks(list_of_tasks=self.list_of_get_call_tasks)


class TestTasksAnotherSetUp(TestTasks):

    def setUp(self) -> None:
        self.list_of_get_call_tasks = [
            unittest.mock.create_autospec(GetCallTask)
            for _ in range(10)
        ]
