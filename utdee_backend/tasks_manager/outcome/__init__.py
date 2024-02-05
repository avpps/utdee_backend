from typing import List, Optional
from traceback import format_exception

from utdee_backend.tasks_manager.task.abstract import AbstractTask


class Outcome:

    def __init__(self, list_of_tasks: List[AbstractTask]):
        self.list_of_tasks = list_of_tasks

    def error_group(self, msg) -> Optional[ExceptionGroup]:
        errors = []
        for task in self.list_of_tasks:
            if task.error:
                errors.append(task.error)
        if not errors:
            return None
        return ExceptionGroup(msg, errors)

    def error_group_traceback_str(self, msg) -> Optional[str]:
        error_group = self.error_group(msg)
        if not error_group:
            return None
        formatted = "".join(format_exception(error_group))
        return formatted

    def error_free_tasks(self) -> List[AbstractTask]:
        return [t for t in self.list_of_tasks if t.error is None]
