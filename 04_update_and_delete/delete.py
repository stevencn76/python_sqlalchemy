from db_init import engine, person_table

with engine.connect() as conn:
    delete_query = person_table.delete().where(person_table.c.id == 7)
    conn.execute(delete_query)
    conn.commit()
