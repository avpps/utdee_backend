import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class RunInfo(Base):
    __tablename__ = "run_info"
    run_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    start: Mapped[datetime.datetime] = mapped_column(DateTime)


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    location: Mapped[str] = mapped_column(String)
    start: Mapped[datetime.datetime] = mapped_column(DateTime)
    temperature: Mapped[float] = mapped_column(Float)
    symbol: Mapped[str] = mapped_column(String)
    updated: Mapped[datetime.datetime] = mapped_column(DateTime)
    run_id: Mapped[str] = mapped_column(ForeignKey("run_info.run_id"))
