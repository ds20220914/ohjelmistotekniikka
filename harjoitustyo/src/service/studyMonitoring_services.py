from repository.user_repository import UserRepository
from entities.user import User

class Services:


	def new_user(self,name,password,role_number):
		user=UserRepository.create(User(name,password,role_number))
		return user



