import unittest
from pathlib import PurePath
from typing import Tuple

import requests_mock

from utdee_backend.api.thread_task_ import urls
from utdee_backend.context import Context
from tests.test_api.integration import IntegrationSetUp
from tests.utils import patch_requests_response, PatchedResponses, PRKey, PRValue

forecast_response_path = PurePath(__file__).parent.parent / "fixtures" / "forecast_response"


class TestThreadTask(IntegrationSetUp):

    class ThreadTaskTestPatchedResponses(PatchedResponses):
        def __init__(self):
            self.mappings = {
                PRKey(url=url, method="get"): PRValue(
                    status_code=200,
                    content=open(forecast_response_path, "rb").read()
                )
                for url in urls
            }

    def api_path(self) -> Tuple[str, str]:
        return "utdee_backend.api.thread_task_", "thread_task"

    def setUp(self):
        super().setUp()
        context = Context()
        context.db_session.scalars.return_value = [type(
            "Weather", (), {"start": "2222-22-22T22:22+00:00", "temperature": 0}
        )()]
        self.expected_result = "<html><pre>2222-22-22T22:22+00:00       0\n</pre></html>"

    @patch_requests_response(
        "utdee_backend.tasks_manager.task.requests_based.requests.get",
        responses=ThreadTaskTestPatchedResponses(),
    )
    def test_thread_task(self, mocked_get):
        result = self.api_func()
        self.assertIsInstance(result, str)
        self.assertEqual(self.expected_result, result)
        self.assertEqual(mocked_get.call_count, 1)

    def test_thread_task_requests_mock(self):

        with open(forecast_response_path, "rb") as file:
            with requests_mock.Mocker() as m:
                m.get(url=requests_mock.ANY, status_code=200, body=file)
                result = self.api_func()
            self.assertIsInstance(result, str)
            self.assertEqual(self.expected_result, result)

    @unittest.skip("for local development use only")
    def test_thread_task_without_requests_patch(self):
        result = self.api_func()
