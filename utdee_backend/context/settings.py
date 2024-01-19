import os


class Settings:
    def __init__(self):
        self.PORT = int(os.getenv("PORT"))

        self.GUNICORN_CERT = os.getenv("GUNICORN_CERT")
        self.GUNICORN_KEY = os.getenv("GUNICORN_KEY")

        self.MONGO_URI = os.getenv("MONGO_URI")
        self.MONGO_TEST_DB = os.getenv("MONGO_TEST_DB")
        self.MONGO_TEST_USER = os.getenv("MONGO_TEST_USER")
        self.MONGO_TEST_USER_PASSWORD = os.getenv("MONGO_TEST_USER_PASSWORD")

        self.MYSQL_DIALECT_DRIVER = os.getenv("MYSQL_DIALECT_DRIVER")
        self.MYSQL_URI = os.getenv("MYSQL_URI")
        self.MYSQL_USER = os.getenv("MYSQL_USER")
        self.MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
        self.MYSQL_DB_NAME = os.getenv("MYSQL_DB_NAME")

        self.SPARK_URL = os.getenv("SPARK_URL")
