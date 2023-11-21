from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session

from db_init import engine, engine2, Department, Employee, User


with Session(engine) as session1, session1.begin(), Session(engine2) as session2, session2.begin():
    dep = Department(name="pop2")
    session1.add(dep)

    user = User(name="hhh2")
    session2.add(user)

