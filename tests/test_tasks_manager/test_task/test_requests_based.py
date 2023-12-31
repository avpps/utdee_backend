import unittest
import unittest.mock as mock

from requests import Response
from sources.tasks_manager import GetCallTask
from tests.utils import patch_requests_response, CommonPatchedResponses


class TestGetCallTask(unittest.TestCase):

    @staticmethod
    def mocked_requests_get(*args, **kwargs):
        response = mock.create_autospec(Response, spec_set=True)
        return response

    def setUp(self) -> None:
        self.url = "https://www.python.org"

    @mock.patch(
        "sources.tasks_manager.task.requests_based.requests.get",
        side_effect=mocked_requests_get
    )
    def test_run(self, mocked_get):
        task = GetCallTask(url=self.url)
        result = task.run()
        mocked_get.assert_called_once()
        self.assertTrue(isinstance(result, Response))
        self.assertTrue(task.result is None)

    # usage of more complex patch approach
    @patch_requests_response(
        path="sources.tasks_manager.task.requests_based.requests.get",
        responses=CommonPatchedResponses(),
    )
    def test_run_another(self, response):
        task = GetCallTask(url=self.url)
        result = task.run()
        self.assertIsInstance(result, Response)
        response.assert_called_once()
        self.assertIsInstance(result.content, bytes)
