from entities.user import User
from database_connection import get_database_connection



class UserRepository:
	def __init__(self, get):

		self._get=get


	def create(self, User):
		 
		ab=self._get.cursor()
		ab.execute("INSERT INTO User (User_name,password,role_number) values (?,?,?)",(User.username,User.password,User.role_number))
		self._get.commit()
		return User
	def find_all(self):
		db=self._get.cursor()
		lista=self._get.execute("SELECT * FROM User ").fetchall()
		return list(lista)
