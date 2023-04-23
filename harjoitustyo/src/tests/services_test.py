from service.studymonitoring_services import Services
import unittest
from repository.user_repository import user_repository
from entities.user import User

class TestService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_eka = User("moi", "1234", "A2222")
        
    def test_new_user(self):
        
        username = "moi"
        password = "1234"
        role_number = "1111"
        uusi = Services()
        uusi.new_user(username, password, role_number)
        lista = user_repository.find_all()
        käyttäjä = lista[0]
        oikea = käyttäjä["User_name"]
        print(oikea)
        self.assertEqual(oikea, "moi")
