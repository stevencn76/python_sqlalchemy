from db_init import engine, person_table

with engine.connect() as conn:
    # update_query = person_table.update().values(address="aaa")
    update_query = person_table.update().values(address="Shanghai").where(person_table.c.id == 6)
    conn.execute(update_query)
    conn.commit()
