import sqlalchemy


engine = sqlalchemy.create_engine('mysql://root:test@localhost/testdb')
conn = engine.connect()

query = sqlalchemy.text('SELECT * FROM students')
result_set = conn.execute(query)

for row in result_set:
    print(row)

conn.close()

engine.dispose()
