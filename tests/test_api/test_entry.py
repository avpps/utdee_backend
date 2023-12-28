import unittest
from typing import Tuple

from tests.test_api.integration import IntegrationSetUp


class TestEntry(IntegrationSetUp):

    def api_path(self) -> Tuple[str, str]:
        return "sources.api.entry_", "entry"

    @unittest.expectedFailure
    def test_entry(self):
        self.api_func()
