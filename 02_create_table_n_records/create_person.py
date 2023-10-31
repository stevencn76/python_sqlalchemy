import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:test@localhost/testdb', echo=True)

meta_data = sqlalchemy.MetaData()

person = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
)

meta_data.create_all(engine)

# insert a record
# person_insert = person.insert()
# print(person_insert)
# insert_tom = person_insert.values(name="TomTom", birthday="2000-10-11")
#
# with engine.connect() as conn:
#     result = conn.execute(insert_tom)
#     print(result.inserted_primary_key)
#     conn.commit()

# insert multiple records
person_insert = person.insert()
with engine.connect() as conn:
    conn.execute(person_insert, [
        {"name": "Jack", "birthday": "2000-10-13"},
        {"name": "Mary", "birthday": "2000-10-14"},
        {"name": "Smith", "birthday": "2000-10-15"},
    ])
    conn.commit()
