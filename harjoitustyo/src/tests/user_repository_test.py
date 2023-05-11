import unittest
from entities.user import User
from repository.user_repository import user_repository
from database_connection import get_course_connection
from database_connection import get_database_connection
import sqlite3


class TestUser(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
        self.user_first = User("moi", "1234", "A2222")

    def test_create_user(self):
        user = User("moi", "1234", "A2222")
        user_repository.create(self.user_first)
        list = user_repository.find_all()
        user = list[0]
        right = user["User_name"]
        print(right)
        self.assertEqual(right, "moi")

    def test_get_database_connection(self):

        connection = get_database_connection()
        self.assertIsNotNone(connection)

    def test_find_by_username(self):
        user = User("moi", "1234", "A2222")
        user_repository.create(self.user_first)
        list = user_repository.find_by_username(user.username)
        sum = len(list)
        self.assertEqual(sum, 1)
    def test_find_all(self):
        user = User("moi1", "1234", "A2222")
        user_repository.create(self.user_first)
        user_repository.create(user)
        list = user_repository.find_all()
        sum = len(list)
        self.assertEqual(sum, 2)
