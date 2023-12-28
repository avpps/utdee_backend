import importlib
import unittest.mock
from abc import ABC, abstractmethod
from typing import Tuple

from tests.utils.context_mock_setup import ContextMock


class IntegrationSetUp(ContextMock, unittest.TestCase, ABC):

    def setUp(self):
        super().setUp()
        api_path, api_func_name = self.api_path()
        # TODO: refactor below patches to make use of them in tests
        unittest.mock.patch(f"{api_path}.otel_trace", lambda x: x).start()
        unittest.mock.patch(f"{api_path}.get", lambda x: x).start()
        api_module = importlib.import_module(api_path)
        self.api_func = getattr(api_module, api_func_name)

    def tearDown(self):
        unittest.mock.patch.stopall()

    @abstractmethod
    def api_path(self) -> Tuple[str, str]:
        pass
