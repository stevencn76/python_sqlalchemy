from db_init import Session, Department, Employee


def insert_records(session):
    d1 = Department(name="hr")
    e1 = Employee(department=d1, name="Jack", birthday="2000-10-1")
    session.add(e1)

    session.commit()


def select_employee(session):
    emp = session.query(Employee).filter(Employee.id == 1).one()

    print(emp)
    print(emp.department)


def select_department(session):
    dep = session.query(Department).filter(Department.id == 1).one()

    print(dep)
    print(dep.employees)


session = Session()

# insert_records(session)
# select_employee(session)
select_department(session)
