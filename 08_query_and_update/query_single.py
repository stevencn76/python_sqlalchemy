from db_init import Session, Person


session = Session()

# person = session.query(Person).filter(Person.address == 'aaa').first()
# person = session.query(Person).filter(Person.id == 100).first()
# person = session.query(Person).filter(Person.id == 1).one()
person = session.query(Person).filter(Person.id == 1).scalar()

if person:
    print(f'name: {person.name}, birthday: {person.birthday}')
