from bottle import route

from sources.utils.trace import otel_trace


@route("/spark_tasks")
@otel_trace
def spark_tasks():
    return ""
