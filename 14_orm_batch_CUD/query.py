from sqlalchemy import select, insert, update, bindparam, delete
from sqlalchemy.orm import Session

from db_init import engine, Department, Employee


def batch_insert():
    with Session(engine) as session:
        session.execute(
            insert(Department).values(
                [
                    {"name": "QA"},
                    {"name": "Sales"}
                ]
            )
        )
        session.commit()


def batch_orm_insert():
    with Session(engine) as session:
        session.execute(
            insert(Employee).values(
                [
                    {
                        "dep_id": select(Department.id).where(Department.name == 'hr'),
                        "name": "wwww",
                        "birthday": "2000-1-19"
                    },
                    {
                        "dep_id": select(Department.id).where(Department.name == 'market'),
                        "name": "YYY",
                        "birthday": "2000-2-19"
                    }
                ]
            )
        )
        session.commit()


def batch_update():
    with Session(engine) as session:
        session.execute(
            update(Employee),
            [
                {"id": 2, "birthday": "1999-2-9"},
                {"id": 5, "name": "Samuel"}
            ]
        )
        session.commit()


def batch_delete():
    with Session(engine) as session:
        session.execute(
            delete(Employee).where(Employee.name.in_(['wwww', 'YYY']))
        )
        session.commit()


batch_delete()
