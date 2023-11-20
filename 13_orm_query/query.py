from sqlalchemy import select, insert, update, bindparam, delete
from sqlalchemy.orm import outerjoin, aliased

from db_init import Session, Department, Employee


def execute_query(query):
    result = session.execute(query)
    for row in result:
        print(row)


def select_single_target():
    query = select(Department).order_by(Department.name)
    execute_query(query)


def select_multiple():
    query = select(Employee, Department).join(Employee.department, isouter=True)
    execute_query(query)


def select_with_alias():
    emp_cls = aliased(Employee, name="emp")
    dep_cls = aliased(Department, name="dep")
    query = select(emp_cls, dep_cls).join(emp_cls.department.of_type(dep_cls))
    execute_query(query)


def select_fields():
    query = select(Employee.name.label('emp_name'), Department.name.label('dep_name')).join_from(Employee, Department)
    execute_query(query)


def select_fields_outer():
    query = select(Employee.name.label('emp_name'), Department.name.label('dep_name'))\
        .select_from(outerjoin(Employee, Department))
    execute_query(query)


def where_obj():
    dep = session.get(Department, 1)
    # query = select(Employee).where(Employee.department == dep)
    query = select(Employee).where(Employee.dep_id != dep.id)
    execute_query(query)


def select_contains():
    emp = session.get(Employee, 1)
    query = select(Department).where(Department.employees.contains(emp))
    execute_query(query)


session = Session()
# select_single_target()
# select_multiple()
# select_with_alias()
# select_fields()
# select_fields_outer()
# where_obj()
select_contains()
