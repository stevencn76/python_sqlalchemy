from db_init import engine, person_table

with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)

    # for row in result_set:
    #     print(row[0])
    #     print(row.name)

    # result = result_set.fetchall()
    # print(result)

    row = result_set.fetchone()
    print(row)
