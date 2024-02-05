from bottle import get

from utdee_backend.tasks_manager import (
    thread_pool_list_of_get_call_tasks,
    GetCallTask, WeatherDataParser, Outcome,
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

    get_tasks_outcome = Outcome(list_of_tasks=list_of_get_tasks)
    get_tasks_errors = get_tasks_outcome.error_group_traceback_str("get_tasks_errors")

    list_of_parsing_tasks = [
        WeatherDataParser(t.result)
        for t in get_tasks_outcome.error_free_tasks()
        if t.error is None

    ]
    thread_pool_list_of_get_call_tasks(list_of_tasks=list_of_parsing_tasks)
    parsing_tasks_outcome = Outcome(list_of_tasks=list_of_parsing_tasks)
    parsing_tasks_errors = parsing_tasks_outcome.error_group_traceback_str("parsing_tasks_errors")

    result = ""
    for parsed in parsing_tasks_outcome.error_free_tasks():
        weather: Weather
        # result += "{}\n".format(run_id)
        # result += "{}\n\n".format(location.capitalize())
        for weather in parsed.result:
            result += f"{str(weather.start):<25}{weather.temperature:>5}\n"

    result = "".join((
        "<html>",
        f"<pre>{result}</pre></br></br></br>",
        f"<pre>{str(get_tasks_errors)}</pre></br></br></br>" if get_tasks_errors else "",
        f"<pre>{str(parsing_tasks_errors)}</pre></br></br></br>" if parsing_tasks_errors else "",
        "</html>",
    ))
    return result
