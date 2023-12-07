from __future__ import annotations
from abc import ABC, abstractmethod

from sources.tasks_manager.dispather.abstract import AbstractTasksDispatcher
from sources.utils.context_manager import ContextManager


class AbstractTasksFactory(ABC, ContextManager):
    dispatcher: AbstractTasksDispatcher

    @abstractmethod
    def start(self):
        pass
