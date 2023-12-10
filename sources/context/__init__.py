from opentelemetry.trace import Tracer

from sources.utils.singleton import Singleton
from sources.context.settings import Settings


class Context(metaclass=Singleton):
    settings: Settings
    tracer: Tracer

    def __init__(self):
        self.settings = Settings()
