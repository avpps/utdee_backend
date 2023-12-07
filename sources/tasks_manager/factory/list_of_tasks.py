from __future__ import annotations
from typing import List

from sources.tasks_manager.task.abstract import AbstractTask
from sources.tasks_manager.factory.abstract import AbstractTasksFactory


class ListOfTasksFactory(AbstractTasksFactory):

    def __init__(self, list_of_tasks: List[AbstractTask]):
        self.list_of_tasks = list_of_tasks

    def start(self):
        for task in self.list_of_tasks:
            self.dispatcher.run_task(task=task)
