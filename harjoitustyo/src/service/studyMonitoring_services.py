from repository.user_repository import user_repository
from entities.user import User
from repository.course_repository import course_repository


class Services:

    def new_user(self, name, password, role_number):

        user = user_repository.create(User(name, password, role_number))
        return user
        
    def find_course_by_username(self,username):
        rolenumber = user_repository.find_by_username(
            username)
        number=None
        for i in rolenumber:
            number=i["role_number"]
        lista=course_repository.find_all_course_by_student_role_number(
            number)
        return lista

    def find_by_rolenumber(self, rolenumber):

        lista = course_repository.find_all_course_by_student_role_number(
            rolenumber)

        return lista

    def find_by_coursename_rolenumber(self, rolenumber, course_name):
        lista = course_repository.find_all_course_by_student_role_number(
            rolenumber)
        for i in lista:
            if course_name == i["Course_name"]:
                return False
        return True

    def login(self, username, password):
        if username[0] == "A":
            lista = user_repository.find_all()
            for i in lista:
                if username == i["User_name"] and password == i["password"]:
                    return 1
        if username[0] == "B":
            lista = user_repository.find_all()
            for i in lista:
                if username == i["User_name"] and password == i["password"]:
                    return 2

    def add_new_course(self, rolenumber, course):
        course_repository.create_course(rolenumber, course)
