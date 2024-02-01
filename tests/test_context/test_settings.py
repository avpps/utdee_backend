from unittest import TestCase
from unittest.mock import patch

from utdee_backend.context.settings import Settings
from tests.utils.context_mock_setup import settings_environ


SETTINGS_ENV = settings_environ()

SETTINGS_ENV_MOD = settings_environ()
SETTINGS_ENV_MOD["ENV_NAME"] = ""


class TestSettings(TestCase):
    def setUp(self):
        pass

    @patch("utdee_backend.context.settings.os.environ", SETTINGS_ENV)
    def test_settings_from_environ(self):
        Settings()


    @patch("utdee_backend.context.settings.os.environ", SETTINGS_ENV_MOD)
    def test_settings_from_files(self):
        Settings()
