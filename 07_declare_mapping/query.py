from db_init import Session, Person


session = Session()

# p = Person(name="Amy", birthday="2000-9-18", address="unknown")
# session.add(p)

person_list = [
    Person(name="Eric", birthday="1998-2-18", address="unknown"),
    Person(name="Samuel", birthday="1997-1-15", address="unknown")
]
session.add_all(person_list)

session.commit()
