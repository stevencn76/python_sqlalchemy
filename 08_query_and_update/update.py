from db_init import Session, Person


session = Session()

# person = session.query(Person).filter(Person.id == 1).one()
# person.address = 'wwww'

# session.query(Person).filter(Person.id == 1).update({
#     Person.address: 'PPPP'
# })

session.query(Person).filter(Person.id > 14).update({
    Person.address: 'Beijing'
})


session.commit()
