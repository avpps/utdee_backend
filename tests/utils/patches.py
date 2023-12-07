import unittest
from unittest import mock as mock


def patch_requests_request_response(path, response):
    def func_wrapper(func):
        @mock.patch(path)
        def wrapper(test_case: unittest.TestCase, request, *args, **kwargs):
            request.return_value = response
            return func(test_case, *args, **kwargs)
        return wrapper
    return func_wrapper
