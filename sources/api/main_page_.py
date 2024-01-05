from bottle import get

from sources.utils.trace import otel_trace


@get("/")
@otel_trace
def main_page():
    return "main_page"
