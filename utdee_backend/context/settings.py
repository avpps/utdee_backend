import os
from pathlib import Path


class  Settings:

    def read_secret(self, file_name):
        if self.ENV_NAME in ("local", "local_test"):
            return os.getenv(file_name)

        file_path = self.SECRETS_PATH / file_name
        if not file_path.exists():
            return None
        with open(file_path, encoding="utf-8") as file:
            return file.read()

    def __init__(self):
        # base
        self.PORT = int(os.getenv("PORT"))
        self.ENV_NAME = os.getenv("ENV_NAME")

        # secrets
        self.SECRETS_PATH = Path(os.getenv("SECRETS_PATH"))

        self.GUNICORN_CERT = str(self.SECRETS_PATH / "GUNICORN_CERT")
        self.GUNICORN_KEY = str(self.SECRETS_PATH / "GUNICORN_KEY")

        self.MONGO_URI = self.read_secret("MONGO_URI")
        self.MONGO_TEST_DB = self.read_secret("MONGO_TEST_DB")
        self.MONGO_TEST_USER = self.read_secret("MONGO_TEST_USER")
        self.MONGO_TEST_USER_PASSWORD = self.read_secret("MONGO_TEST_USER_PASSWORD")

        self.MYSQL_DIALECT_DRIVER = self.read_secret("MYSQL_DIALECT_DRIVER")
        self.MYSQL_URI = self.read_secret("MYSQL_URI")
        self.MYSQL_USER = self.read_secret("MYSQL_USER")
        self.MYSQL_PASSWORD = self.read_secret("MYSQL_PASSWORD")
        self.MYSQL_DB_NAME = self.read_secret("MYSQL_DB_NAME")

        self.SPARK_URL = self.read_secret("SPARK_URL")
