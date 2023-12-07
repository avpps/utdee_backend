from typing import List

from sources import otel_trace
from sources.tasks_manager import (
    TasksManager,
    ListOfTasksFactory,
    ThreadPoolTasksDispatcher, ProcessPoolTasksDispatcher,
    GetCallTask,
)


@otel_trace
def thread_pool_list_of_get_call_tasks(list_of_tasks: List[GetCallTask]):
    factory = ListOfTasksFactory(list_of_tasks=list_of_tasks)
    dispatcher = ThreadPoolTasksDispatcher()
    with TasksManager(
        factory=factory,
        dispatcher=dispatcher,
    ) as manager:
        manager.run()


@otel_trace
def process_pool_list_of_get_call_tasks(list_of_tasks: List[GetCallTask]):
    factory = ListOfTasksFactory(list_of_tasks=list_of_tasks)
    dispatcher = ProcessPoolTasksDispatcher()
    with TasksManager(
        factory=factory,
        dispatcher=dispatcher,
    ) as manager:
        manager.run()
