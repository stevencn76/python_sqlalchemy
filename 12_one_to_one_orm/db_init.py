import datetime

from sqlalchemy import create_engine, String, ForeignKey, Table, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from typing_extensions import Annotated
from typing import List, Set


engine = create_engine('mysql://root:test@localhost/testdb', echo=True)
Base = declarative_base()


int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_string = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
required_string = Annotated[str, mapped_column(String(128), nullable=False)]


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int_pk]
    name: Mapped[required_unique_string]
    computer_id: Mapped[int] = mapped_column(ForeignKey("computer.id"), nullable=True)

    computer = relationship("Computer", lazy=False, back_populates="employee")

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


class Computer(Base):
    __tablename__ = "computer"

    id: Mapped[int_pk]
    model: Mapped[required_string]
    number: Mapped[required_unique_string]

    employee = relationship("Employee", lazy=True, back_populates="computer")

    def __repr__(self):
        return f'id: {self.id}, model: {self.model}, number: {self.number}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
