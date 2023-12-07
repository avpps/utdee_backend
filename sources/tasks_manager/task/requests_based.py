import requests

from sources.tasks_manager.task.abstract import AbstractTask


class GetCallTask(AbstractTask):

    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url, timeout=5)
        response.raise_for_status()
        return response
