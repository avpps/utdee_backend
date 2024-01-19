import uuid
from types import SimpleNamespace

import pendulum
from sqlalchemy import select

from utdee_backend.context import Context
from utdee_backend.db.orm import RunInfo, Weather
from utdee_backend.tasks_manager.task.abstract import AbstractTask, run_exception_handler


class WeatherDataParser(AbstractTask):

    def __init__(self, input_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_data = input_data
        self.db_session = Context().db_session

    @run_exception_handler()
    def run(self):

        # TODO: support real uuid of run:
        run_id = str(uuid.uuid4())
        self.db_session.add(RunInfo(
            run_id=run_id,
            start=pendulum.now()
        ))

        location = "warsaw"
        fo = self.input_data.json(object_hook=lambda d: SimpleNamespace(**d))
        for sh in fo.shortIntervals:
            self.db_session.add(Weather(
                location=location,
                start=pendulum.parse(sh.start),
                temperature=sh.temperature.value,
                symbol=sh.symbol,
                updated=pendulum.parse(fo.update),
                run_id=run_id,
            ))
        self.db_session.commit()

        result = list(self.db_session.scalars(
            select(Weather)
            .where(Weather.location == location)
            .where(Weather.run_id == run_id)
            .order_by(Weather.start)
        ))
        return result
