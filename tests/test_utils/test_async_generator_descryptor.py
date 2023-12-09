import unittest
from typing import AsyncGenerator

from sources.utils.async_generator_descryptor import AsyncGeneratorDescriptor


class TestAsyncGeneratorDescriptor(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.list_of_values = list("asdf")
        self.instance = type("Instance", (), {"attr": AsyncGeneratorDescriptor()})()

    def test_base(self):
        self.instance.attr = self.list_of_values

        self.assertTrue(hasattr(self.instance, "_attr"))
        self.assertTrue(hasattr(self.instance, "attr"))

        self.assertTrue(getattr(self.instance, "_attr") is self.list_of_values)
        self.assertIsInstance(self.instance.attr, AsyncGenerator)

    async def test_generator(self):
        self.instance.attr = self.list_of_values
        result = []
        async for v in self.instance.attr:
            result.append(v)
        self.assertSequenceEqual(result, self.list_of_values)
