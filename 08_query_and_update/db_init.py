from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://root:test@localhost/testdb', echo=True)
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    birthday = Column(Date, nullable=False)
    address = Column(String(255), nullable=True)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
