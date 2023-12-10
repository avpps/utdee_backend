import asyncio

import pyspark

from sources.context import Context
from sources.tasks_manager.task.abstract import AbstractTask
from sources.tasks_manager.dispather.abstract import AbstractTasksDispatcher
from sources.utils.trace import otel_trace


class SparkDispatcher(AbstractTasksDispatcher):

    def __enter__(self):
        context = Context()
        self.spark = pyspark.sql.SparkSession.builder.remote(context.settings.SPARK_URL).getOrCreate()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spark.stop()

    @otel_trace
    async def run_task(self, task: AbstractTask):
        pass
