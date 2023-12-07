from __future__ import annotations
from abc import ABC, abstractmethod

# TODO: circular import
# from sources.tasks_manager.factory import AbstractTasksFactory
from sources.tasks_manager.task.abstract import AbstractTask
from sources.utils.context_manager import ContextManager


class AbstractTasksDispatcher(ABC, ContextManager):
    tasks_factory: "AbstractTasksFactory"

    @abstractmethod
    def run_task(self, task: AbstractTask):
        pass
