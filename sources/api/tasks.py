from typing import List

from sources.tasks_manager import (
    TasksManager,
    ListOfTasksFactory,
    ThreadPoolTasksDispatcher, ProcessPoolTasksDispatcher,
    GetCallTask,
)


def thread_pool_list_of_get_call_tasks(list_of_tasks: List[GetCallTask]):
    factory = ListOfTasksFactory(list_of_tasks=list_of_tasks)
    dispatcher = ThreadPoolTasksDispatcher()
    with TasksManager(
        factory=factory,
        dispatcher=dispatcher,
    ) as manager:
        manager.run()


def process_pool_list_of_get_call_tasks(list_of_tasks: List[GetCallTask]):
    factory = ListOfTasksFactory(list_of_tasks=list_of_tasks)
    dispatcher = ProcessPoolTasksDispatcher()
    with TasksManager(
        factory=factory,
        dispatcher=dispatcher,
    ) as manager:
        manager.run()
