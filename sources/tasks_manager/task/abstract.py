from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractTask(ABC):

    def __init__(self, *args, **kwargs):
        self.result = None

    @abstractmethod
    def run(self):
        pass
