import unittest
import unittest.mock as mock

from sources.tasks_manager.api.tasks import (
    thread_pool_list_of_get_call_tasks,
    process_pool_list_of_get_call_tasks,
)
from sources.tasks_manager import GetCallTask
from tests.utils import ContextMock


class TestTasks(ContextMock, unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.list_of_get_call_tasks = [
            type("GetCallTask", (GetCallTask, ), {"run": mock.MagicMock(name="run")})
            for _ in range(10)
        ]

    def test_thread_pool_tasks(self):
        thread_pool_list_of_get_call_tasks(list_of_tasks=self.list_of_get_call_tasks)
        for result in self.list_of_get_call_tasks:
            result.run.assert_called_once()

    @unittest.SkipTest
    def test_process_pool_tasks(self):
        process_pool_list_of_get_call_tasks(list_of_tasks=self.list_of_get_call_tasks)
