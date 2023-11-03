from db_init import engine, department, employee

with engine.connect() as conn:
    conn.execute(department.insert(), [
        {"name": "hr"}, {"name": "it"}
    ])

    conn.execute(employee.insert(), [
        {"department_id": 1, "name": "Jack"},
        {"department_id": 1, "name": "Tom"},
        {"department_id": 1, "name": "Mary"},
        {"department_id": 2, "name": "Smith"},
        {"department_id": 2, "name": "Rose"},
        {"department_id": 2, "name": "Leon"},
    ])

    conn.commit()

