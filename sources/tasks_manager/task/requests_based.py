import requests
from requests.models import Response

from sources.tasks_manager.task.abstract import AbstractTask


class GetCallTask(AbstractTask):
    result: Response

    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url, timeout=5)
        response.raise_for_status()
        return response
