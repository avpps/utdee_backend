from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from utdee_backend.context import Context


def db_session_class(db_engine):
    return sessionmaker(bind=db_engine)


def db_engine():
    context = Context()
    return create_engine(
        url="{}://{}:{}@{}/{}".format(
            context.settings.MYSQL_DIALECT_DRIVER,
            context.settings.MYSQL_USER,
            context.settings.MYSQL_PASSWORD,
            context.settings.MYSQL_URI,
            context.settings.MYSQL_DB_NAME,
        ),
        # echo=True,
    )


def db_session_class_mock():
    from unittest.mock import create_autospec
    return create_autospec(Session)
