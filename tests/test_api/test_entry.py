import unittest.mock
from typing import Tuple

from pymongo.errors import InvalidURI

from tests.test_api.integration import IntegrationSetUp


class TestEntry(IntegrationSetUp):

    def api_path(self) -> Tuple[str, str]:
        return "sources.api.entry_", "entry"

    @unittest.mock.patch("builtins.open", unittest.mock.MagicMock())
    def test_entry(self):
        with self.assertRaises(InvalidURI):
            self.api_func()
        self.assertEqual(open.call_count, 1)
