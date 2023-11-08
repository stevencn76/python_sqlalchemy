import datetime

from sqlalchemy import create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column
from sqlalchemy.sql import func
from typing_extensions import Annotated


engine = create_engine('mysql://root:test@localhost/testdb', echo=True)
Base = declarative_base()


int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
timestamp_default_now = Annotated[datetime.datetime, mapped_column(nullable=False, server_default=func.now())]


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    birthday: Mapped[datetime.datetime]
    city: Mapped[str] = mapped_column(String(128), nullable=True)
    create_time: Mapped[timestamp_default_now]


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
