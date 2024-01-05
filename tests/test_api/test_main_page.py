from typing import Tuple

from tests.test_api.integration import IntegrationSetUp


class TestEntry(IntegrationSetUp):

    def api_path(self) -> Tuple[str, str]:
        return "sources.api.main_page_", "main_page"

    def test_entry(self):
        result = self.api_func()
        self.assertEqual(result, "main_page")
