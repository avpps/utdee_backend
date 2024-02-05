from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


def run_exception_handler(*pargs, **pkwargs):  # noqa
    def wrapper(run):
        def run_wrapper(task: AbstractTask, *args, **kwargs):
            try:
                result = run(task, *args, **kwargs)
                return result
            except Exception as e:
                task.error = e
                raise e
        return run_wrapper
    return wrapper


class AbstractTask(ABC):

    def __init__(self, *args, **kwargs):  # noqa
        self.result = None
        self.error: Optional[Exception] = None

    @abstractmethod
    @run_exception_handler()
    def run(self):
        pass
