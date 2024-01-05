import asyncio
from unittest import IsolatedAsyncioTestCase

from sources.utils.async_generator_descryptor import async_generator
from sources.tasks_manager.dispather import ThreadPoolTasksDispatcher, TaskDispatcherRunResult
from sources.tasks_manager.task.abstract import AbstractTask, run_exception_handler
from tests.utils import ContextMock


class PassingTask(AbstractTask):

    @run_exception_handler()
    def run(self):
        return ""


class FailingTask(AbstractTask):

    class FailingTaskException(Exception):
        pass

    @run_exception_handler()
    def run(self):
        raise self.FailingTaskException()


class TestThreadPoolBased(ContextMock, IsolatedAsyncioTestCase):

    def setUp(self):
        super().setUp()
        self.simple_task = PassingTask()
        self.failing_task = FailingTask()

    async def test_base(self):
        with ThreadPoolTasksDispatcher() as dispatcher:
            await dispatcher.run_task(self.simple_task)

            self.assertEqual(len(dispatcher.run_result), 1)
            result = dispatcher.run_result[0]
            self.assertIsInstance(result, TaskDispatcherRunResult)
            self.assertIsNone(result.exception)
            self.assertIsInstance(result.task, AbstractTask)

    async def test_multiple(self):
        samples = 30
        with ThreadPoolTasksDispatcher() as dispatcher:
            async with asyncio.TaskGroup() as tg:
                async for _ in async_generator(samples):
                    tg.create_task(dispatcher.run_task(self.simple_task))

            self.assertEqual(len(dispatcher.run_result), samples)
            for i in range(samples):
                result = dispatcher.run_result[i]
                self.assertIsInstance(result, TaskDispatcherRunResult)
                self.assertIsNone(result.exception)
                self.assertIsInstance(result.task, AbstractTask)
                # TODO: checkout thread identifiers to ensure they worked as expected

    async def test_failed_task(self):
        with ThreadPoolTasksDispatcher() as dispatcher:
            await dispatcher.run_task(self.failing_task)

            self.assertEqual(len(dispatcher.run_result), 1)
            result = dispatcher.run_result[0]
            self.assertIsInstance(result, TaskDispatcherRunResult)
            self.assertIsInstance(result.exception, FailingTask.FailingTaskException)
            self.assertIsInstance(result.task, AbstractTask)
