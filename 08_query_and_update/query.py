from db_init import Session, Person


session = Session()

# result = session.query(Person).all()
result = session.query(Person).filter(Person.address == 'aaa')

for person in result:
    print(f'name: {person.name}, birthday: {person.birthday}')
