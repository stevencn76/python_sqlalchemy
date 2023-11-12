from db_init import Session, Employee, Computer


def insert(s):
    c1 = Computer(model="Dell", number="1111")
    c2 = Computer(model="Surface", number="2222")
    c3 = Computer(model="MacBook Pro", number="3333")

    e1 = Employee(name="Jack", computer=c1)
    e2 = Employee(name="Mary", computer=c2)
    e3 = Employee(name="Tome", computer=c3)

    s.add_all([e1, e2, e3])

    s.commit()


def select(s):
    e = s.query(Employee).filter(Employee.id == 1).scalar()
    if e:
        print(e)
        print(e.computer)

    c = s.query(Computer).filter(Computer.id == 2).scalar()
    if c:
        print(c)
        print(c.employee)


def update_1(s):
    s.query(Employee).filter(Employee.id == 3).update({Employee.computer_id: None})
    s.commit()


def update_2(s):
    c = s.query(Computer).filter(Computer.id == 3).scalar()
    e = s.query(Employee).filter(Employee.id == 3).scalar()
    if c and e:
        e.computer = c
        s.commit()


session = Session()
# insert(session)
# select(session)
# update_1(session)
update_2(session)
