from database_connection import get_database_connection
from database_connection import get_course_connection


class UserRepository:
    def __init__(self, connection1, connection2):
        self._connection1 = connection1
        self._connection2 = connection2

    def create(self, user):
        db_connection = self._connection1.cursor()
        db_connection.execute("INSERT INTO User (User_name, password, role_number) "
                              "VALUES (?, ?, ?)",
                              (user.username, user.password, user.role_number))
        self._connection1.commit()
        return user

    def find_all(self):
        db_connection = self._connection1.cursor()
        lista = db_connection.execute("SELECT * FROM User ").fetchall()
        return list(lista)
    def find_by_username(self,username):
        db_connection = self._connection1.cursor()
        lista = db_connection.execute("SELECT * FROM User WHERE User_name=?",(username,)).fetchall()
        return lista
    def delete_all(self):
        cursor = self._connection1.cursor()
        cursor.execute("delete from User")
        self._connection1.commit()


user_repository = UserRepository(
    get_database_connection(), get_course_connection())
