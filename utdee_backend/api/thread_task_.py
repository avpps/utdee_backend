from bottle import get

from utdee_backend.tasks_manager import (
    thread_pool_list_of_get_call_tasks,
    GetCallTask, WeatherDataParser,
)
from utdee_backend.db.orm import Weather
from utdee_backend.utils.trace import otel_trace


urls = (
    "https://www.yr.no/api/v0/locations/2-7531926/forecast",
)


@get("/thread_task")
@otel_trace
def thread_task():
    list_of_get_tasks = [GetCallTask(u) for u in urls]
    thread_pool_list_of_get_call_tasks(list_of_tasks=list_of_get_tasks)

    list_of_parsing_tasks = [
        WeatherDataParser(t.result)
        for t in list_of_get_tasks
        if t.error is None

    ]
    thread_pool_list_of_get_call_tasks(list_of_tasks=list_of_parsing_tasks)

    result = ""
    for parsed in list_of_parsing_tasks:
        weather: Weather
        # result += "{}\n".format(run_id)
        # result += "{}\n\n".format(location.capitalize())
        for weather in parsed.result:
            result += f"{str(weather.start):<25}{weather.temperature:>5}\n"

    return f"<html><pre>{result}</pre></html>"
