import unittest
from entities.user import User
from service.studyMonitoring_services import Services
from repository.user_repository  import user_repository
from build import build	

class TestUser(unittest.TestCase):
	def setUp(self):
		self.user_eka=User("moi","1234","A2222")

	def test_hello_world(self):
        	self.assertEqual("Hello world", "Hello world")

	def test_create_user(self):
		user=User("moi","1234","A2222")
		user_repository.create(self.user_eka)
		lista=user_repository.find_all()
		self.assertEqual(user.username,"moi")
		
