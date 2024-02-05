from unittest import TestCase

from requests import HTTPError
from utdee_backend.tasks_manager import Outcome, GetCallTask


class TestOutcome(TestCase):

    @staticmethod
    def create_task(url, error_message=None):
        task = GetCallTask(url)
        if error_message:
            task.error = HTTPError(error_message)
        return task

    def setUp(self):
        self.fail_1_str = "fail 1"
        self.fail_2_str = "fail 2"
        self.task_1_failing = self.create_task("url_failing_1", self.fail_1_str)
        self.task_1 = self.create_task("url_1")
        self.task_2_failing = self.create_task("url_failing_2", self.fail_2_str)
        self.task_2 = self.create_task("url_2")
        self.tasks = [
            self.task_1_failing,
            self.task_1,
            self.task_2_failing,
            self.task_2,
        ]

    def test_init(self):
        Outcome(list_of_tasks=self.tasks)

    def test_error_group(self):
        outcome = Outcome(list_of_tasks=self.tasks)
        error_group = outcome.error_group("some message")
        self.assertIsInstance(error_group, ExceptionGroup)
        with self.assertRaises(ExceptionGroup):
            raise error_group

    def test_error_group_traceback(self):
        outcome = Outcome(list_of_tasks=self.tasks)
        group_message = "some message"
        traceback_str = outcome.error_group_traceback_str(group_message)
        self.assertIsInstance(traceback_str, str)
        self.assertTrue(group_message in traceback_str)
        self.assertTrue(self.fail_1_str in traceback_str)
        self.assertTrue(self.fail_2_str in traceback_str)

    def test_error_free_tasks(self):
        outcome = Outcome(list_of_tasks=self.tasks)
        error_free = outcome.error_free_tasks()
        self.assertListEqual(error_free, [self.task_1, self.task_2])
