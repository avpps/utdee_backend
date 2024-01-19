import unittest

import uuid
import pendulum
from sqlalchemy import select

from tests.utils import ContextMock
from utdee_backend.db.orm import (
    RunInfo,
    Weather,
)


class TestModels(ContextMock, unittest.TestCase):
    """TODO: https://docs.sqlalchemy.org/en/20/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites"""

    def test_run_info(self):
        run_id = str(uuid.uuid4())
        start = pendulum.now()
        ri = RunInfo(
            run_id=run_id,
            start=start,
        )
        self.context.db_session.add(ri)
        self.context.db_session.commit()

    def test_weather(self):
        run_id = str(uuid.uuid4())
        start = pendulum.now()

        ri = RunInfo(
            run_id=run_id,
            start=start,
        )
        self.context.db_session.add(ri)

        location = "test_location"
        w = Weather(
            location=location,
            start=start,
            temperature=0,
            symbol="test_symbol",
            updated=start,
            run_id=run_id,
        )
        self.context.db_session.add(w)
        self.context.db_session.commit()

        self.context.db_session.scalars(
            select(Weather)
            .where(Weather.location == location)
            .where(Weather.run_id == run_id)
        )
