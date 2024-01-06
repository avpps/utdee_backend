from sources.context import Context
from sources.tasks_manager.task.abstract import AbstractTask
from sources.tasks_manager.dispather.abstract import (
    AbstractTasksDispatcher,
    run_task_exception_handler
)
from sources.utils.trace import otel_trace


class SparkDispatcher(AbstractTasksDispatcher):

    def __enter__(self):
        try:
            import pyspark
        except ImportError:
            raise NotImplementedError()
        context = Context()
        self.spark = pyspark.sql.SparkSession.builder.remote(context.settings.SPARK_URL).getOrCreate()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spark.stop()

    @otel_trace
    @run_task_exception_handler()
    async def run_task(self, task: AbstractTask):
        pass
