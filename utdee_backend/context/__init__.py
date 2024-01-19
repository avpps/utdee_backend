from opentelemetry.trace import Tracer
from sqlalchemy.orm import Session

from utdee_backend.utils.singleton import Singleton
from utdee_backend.context.settings import Settings


class Context(metaclass=Singleton):
    settings: Settings

    tracer: Tracer

    db_session_class: Session
    db_session: Session

    def __init__(self):
        self.settings = Settings()
