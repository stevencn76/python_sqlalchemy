import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:test@localhost/testdb', echo=True)

meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.String(255), nullable=True),
)

meta_data.create_all(engine)
