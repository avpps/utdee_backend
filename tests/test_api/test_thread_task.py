from typing import Tuple

from utdee_backend.api.thread_task_ import urls
from tests.test_api.integration import IntegrationSetUp
from tests.utils import patch_requests_response, PatchedResponses, PRKey, PRValue


class ThreadTaskTestPatchedResponses(PatchedResponses):
    def __init__(self):
        self.mappings = {
            PRKey(url=url, method="get"): PRValue(status_code=200, content=b"")
            for url in urls
        }


class TestThreadTask(IntegrationSetUp):

    def api_path(self) -> Tuple[str, str]:
        return "utdee_backend.api.thread_task_", "thread_task"

    @patch_requests_response(
        "utdee_backend.tasks_manager.task.requests_based.requests.get",
        responses=ThreadTaskTestPatchedResponses(),
    )
    def test_thread_task(self, mocked_get):
        result = self.api_func()
        self.assertIsInstance(result, str)
        self.assertEqual(mocked_get.call_count, 30)
