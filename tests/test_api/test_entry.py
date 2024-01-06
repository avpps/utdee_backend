from typing import Tuple

from tests.test_api.integration import IntegrationSetUp


class TestEntry(IntegrationSetUp):

    def api_path(self) -> Tuple[str, str]:
        return "utdee_backend.api.entry_", "entry"

    def test_entry(self):
        result = self.api_func()
        self.assertTrue(isinstance(result, str))
        self.assertTrue(len(result) > 1)
