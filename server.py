from db import Database_Connection

DB_CON = Database_Connection()


def gets_users():
    users_list = DB_CON.get_users()
    print(users_list)

gets_users()
