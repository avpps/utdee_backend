import unittest
from abc import ABC
from unittest import mock as mock
from typing import Dict

import requests


class PRKey:
    def __init__(self, url: str, method: str = None):
        self.url = url
        self.method = method

    def __hash__(self):
        return hash((self.url, self.method))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class PRValue:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


class PatchedResponses(ABC):
    mappings: Dict[PRKey, PRValue]

    def response(self, *args, **kwargs):
        response_params = self.mappings[PRKey(url=args[0], method="get")]
        response = mock.create_autospec(requests.Response)
        response.patched_responses = self
        response.status_code = response_params.status_code
        response.content = response_params.content
        return response


def patch_requests_response(path, responses: PatchedResponses):
    def func_wrapper(func):
        @mock.patch(path, side_effect=responses.response)
        def wrapper(test_case: unittest.TestCase, response, *args, **kwargs):
            return func(test_case, response, *args, **kwargs)
        return wrapper
    return func_wrapper
