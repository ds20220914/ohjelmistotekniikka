from tkinter import Tk, ttk
from ui.login_view import LoginView
from ui.teacher_view import TeacherView
from ui.teacher_view1 import TeacherView1
from ui.student_view import StudentView
from ui.new_course_view import NewCourseView
from ui.Create_user_view import Create_user
from database_connection import get_database_connection
from repository.user_repository import user_repository
from service.studymonitoring_services import Services


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._ero = None

    def start(self):
        oikea = True
        self.start_login_view(oikea)

    def close_login_view(self):
        username = self._current_view.username_entry.get()
        password = self._current_view.password_entry.get()

        self._current_view.destroy()
        luku = Services()
        luku2 = luku.login(username, password)
        oikea = None
        if luku2 == 1:
            oikea = True
            self._current_view = TeacherView(
                self._root, self.check_student, self.add_new_course, self.logout)

            self._current_view.pack()
        if luku2 == 2:
            oikea = True
            self._current_view = StudentView(
                self._root, self.logout, username)

            self._current_view.pack()
        else:
            oikea = False
            if luku2 != 1 and luku2 != 2:
                self._current_view = LoginView(
                    self._root, self.close_login_view, self.create_user_view, oikea)

                self._current_view.pack()

    def create_user_view(self):
        self._current_view.destroy()
        self._current_view = Create_user(self._root, self.logout)
        self._current_view.pack()

    def logout(self):
        oikea = True
        self._current_view.destroy()
        self.start_login_view(oikea)

    def start_login_view(self, oikea):
        oikea = True
        self._current_view = LoginView(
            self._root, self.close_login_view, self.create_user_view, oikea)

        self._current_view.pack()

    def check_student(self):
        number = self._current_view.rolenumber_entry.get()
        array = Services()
        array1 = array.find_by_rolenumber(number)
        right = None
        if len(array1) == 0:
            right = False
        if len(array1) != 0:
            right = True
        self._current_view.destroy()
        self._current_view = TeacherView1(
            self._root, right, number, self.logout)
        self._current_view.pack()

    def add_new_course(self):
        self._current_view.destroy()
        self._current_view = NewCourseView(self._root, self.logout)
        self._current_view.pack()
