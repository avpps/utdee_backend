from sources.utils.singleton import Singleton
from opentelemetry.trace import Tracer


class Context(metaclass=Singleton):
    tracer: Tracer
