from concurrent.futures import ThreadPoolExecutor

from sources.tasks_manager.task.abstract import AbstractTask
from sources.tasks_manager.dispather.abstract import AbstractTasksDispatcher


class ThreadPoolTasksDispatcher(AbstractTasksDispatcher):

    def __enter__(self):
        self.executor = ThreadPoolExecutor(
            max_workers=10,
            thread_name_prefix=self.__class__.__name__,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.executor.shutdown()

    def run_task(self, task: AbstractTask):
        result = self.executor.submit(task.run)
        task.result = result.result()
