from bottle import route

from sources.tasks_manager import spark_list_of_get_call_tasks
from sources.utils.trace import otel_trace


@route("/spark_task")
@otel_trace
def spark_task():
    spark_list_of_get_call_tasks()
    return ""
