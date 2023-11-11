import datetime

from sqlalchemy import create_engine, String, ForeignKey, Table, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from typing_extensions import Annotated
from typing import List, Set


engine = create_engine('mysql://root:test@localhost/testdb', echo=True)
Base = declarative_base()


int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
required_string = Annotated[str, mapped_column(String(128), nullable=False)]


association_table = Table(
    "user_role",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    password: Mapped[required_string]

    roles: Mapped[List["Role"]] = relationship(secondary=association_table, lazy=False, back_populates="users")

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]

    users: Mapped[List["User"]] = relationship(secondary=association_table, lazy=True, back_populates="roles")

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
