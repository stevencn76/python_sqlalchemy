from db_init import Session, User, Role


def insert_records(s):
    role1 = Role(name="Admin")
    role2 = Role(name="Operator")

    user1 = User(name="Jack", password="111")
    user2 = User(name="Tom", password="222")
    user3 = User(name="Mary", password="333")

    user1.roles.append(role1)
    user1.roles.append(role2)

    user2.roles.append(role1)
    user3.roles.append(role2)

    s.add_all([user1, user2, user3])

    s.commit()


def select_user(s):
    u = s.query(User).filter(User.id == 1).one()
    print(u)
    print(u.roles)


def select_role(s):
    r = s.query(Role).filter(Role.id == 2).one()
    print(r)
    print(r.users)


session = Session()
# insert_records(session)
# select_user(session)
select_role(session)
