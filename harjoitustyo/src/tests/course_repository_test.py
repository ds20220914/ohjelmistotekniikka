import unittest
from entities.course import Course
from repository.course_repository import course_repository
from database_connection import get_course_connection
from database_connection import get_database_connection
import sqlite3


class TestCourse(unittest.TestCase):
    def setUp(self):
        course_repository.delete_all()
        self.course_first = Course("math", 5, 5)
        self.role_number="1234"
    def test_create_course(self):
        course_repository.create_course(self.role_number,self.course_first)
        list = course_repository.find_all_course()
        courses = list[0]
        name = courses["Course_name"]
        print(name)
        self.assertEqual(name, "math")

    def test_find_all_course(self):
        course_repository.create_course(self.role_number,self.course_first)
        list = course_repository.find_all_course()
        courses = list[0]
        name = courses["Course_name"]
        print(name)
        self.assertEqual(name, "math")
    def test_find_all_course_by_student_role_number(self):
        course_repository.create_course(self.role_number,self.course_first)
        list = course_repository.find_all_course_by_student_role_number(self.role_number)
        courses = list[0]
        name = courses["Course_name"]
        print(name)
        self.assertEqual(name, "math")
