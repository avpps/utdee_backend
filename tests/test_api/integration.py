import importlib
from abc import ABC, abstractmethod
from typing import Tuple
from unittest import TestCase
from unittest.mock import patch, mock_open

import mongomock

from tests.utils.context_mock_setup import ContextMock


builtins_open = open


def integration_mock_open(*args, **kwargs):
    if args[0] == "":
        return mock_open(read_data="")(*args, **kwargs)
    return builtins_open(*args, **kwargs)


class IntegrationSetUp(ContextMock, TestCase, ABC):

    def setUp(self):
        super().setUp()

        api_path, api_func_name = self.api_path()
        # TODO: refactor below to make use of patched decorators in tests
        patch(f"{api_path}.otel_trace", lambda x: x).start()
        patch(f"{api_path}.get", lambda x: x).start()

        patch("builtins.open", integration_mock_open).start()

        mongomock.patch(on_new="create").start()

        api_module = importlib.import_module(api_path)
        self.api_func = getattr(api_module, api_func_name)

    def tearDown(self):
        patch.stopall()

    @abstractmethod
    def api_path(self) -> Tuple[str, str]:
        pass
