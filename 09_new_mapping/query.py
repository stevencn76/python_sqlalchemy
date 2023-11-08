from db_init import Session, Customer


session = Session()

c = Customer(name="Jack", birthday="2000-10-1")

session.add(c)

session.commit()
