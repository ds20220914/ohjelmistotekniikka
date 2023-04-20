import unittest
from entities.user import User
from repository.user_repository import user_repository
from database_connection import get_course_connection
from database_connection import get_database_connection
import sqlite3

class TestUser(unittest.TestCase):
    

    def setUp(self):
        user_repository.delete_all()
        self.user_eka = User("moi", "1234", "A2222")

    def test_create_user(self):
        user = User("moi", "1234", "A2222")
        user_repository.create(self.user_eka)
        lista = user_repository.find_all()
        käyttäjä = lista[0]
        oikea = käyttäjä["User_name"]
        print(oikea)
        self.assertEqual(oikea, "moi")

    def test_get_database_connection(self):

        connection = get_database_connection()
        self.assertIsNotNone(connection)
