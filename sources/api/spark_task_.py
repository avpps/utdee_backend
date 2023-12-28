from bottle import get

from sources.tasks_manager import spark_list_of_get_call_tasks
from sources.utils.trace import otel_trace


@get("/spark_task")
@otel_trace
def spark_task():
    spark_list_of_get_call_tasks()
    return ""
