from entities.user import User
from database_connection import get_database_connection
from database_connection import get_course_connection


class CourseRepository:
    def __init__(self, connection1, connection2):

        self._connection1 = connection1
        self._connection2 = connection2

    def create_course(self, role_number, course):
        db_connection = self._connection2.cursor()
        db_connection.execute("INSERT INTO Course (Role_number, Course_name, grade, credit) "
                              "VALUES (?, ?, ?, ?)",
                              (role_number, course.course_name, course.grade, course.credits))
        self._connection2.commit()
        return User

    def find_all_course(self):
        db_connection = self._connection2.cursor()
        lista = db_connection.execute("SELECT * FROM Course ").fetchall()
        return list(lista)

    def find_all_course_by_student_role_number(self, rolenumber):
        db_connection = self._connection2.cursor()
        lista = db_connection.execute(
            "SELECT * FROM Course WHERE Role_number=?", (rolenumber,)).fetchall()
        return list(lista)


course_repository = CourseRepository(
    get_database_connection(), get_course_connection())
