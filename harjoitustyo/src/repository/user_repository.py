from entities.user import User
from database_connection import get_database_connection



class UserRepository:
	def __init__(self,get):

		self.get=get


	def create(self,user): 
		db=get_database_connection()
		db.execute("INSERT INTO User (username,password,role_number) values (?,?,?)",(user.username,user.password,user.role_number))
	def find_all(self):
		lista=self.get.execute("SELECT * FROM User ").fetchall()
		return list(lista))
