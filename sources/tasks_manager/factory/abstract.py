from __future__ import annotations
import asyncio
from abc import ABC, abstractmethod

from sources.tasks_manager.dispather.abstract import AbstractTasksDispatcher
from sources.utils.context_manager import ContextManager


class AbstractTasksFactory(ABC, ContextManager):
    dispatcher: AbstractTasksDispatcher

    def start(self):
        with asyncio.Runner() as runner:
            runner.run(self._start())

    @abstractmethod
    async def _start(self):
        pass
