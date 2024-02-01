from unittest.mock import create_autospec

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from utdee_backend.context import Context


def db_session_class(_db_engine):
    return sessionmaker(bind=_db_engine)


def db_engine():
    s = Context().settings
    return create_engine(
        url="{}://{}:{}@{}/{}".format(  # noqa
            s.MYSQL_DIALECT_DRIVER,
            s.MYSQL_USER,
            s.MYSQL_PASSWORD,
            s.MYSQL_URI,
            s.MYSQL_DB_NAME,
        ),
        # echo=True,
    )


def db_session_class_mock():
    return create_autospec(Session)
