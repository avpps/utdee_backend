from __future__ import annotations
from concurrent.futures import ProcessPoolExecutor

from sources.tasks_manager.task.abstract import AbstractTask
from sources.tasks_manager.dispather.abstract import AbstractTasksDispatcher


class ProcessPoolTasksDispatcher(AbstractTasksDispatcher):

    def __enter__(self):
        self.executor = ProcessPoolExecutor(
            max_workers=10,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.executor.shutdown()

    def run_task(self, task: AbstractTask):
        self.executor.submit(task.run)
