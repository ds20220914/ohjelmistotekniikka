from entities.user import User
from database_connection import get_database_connection



class UserRepository:
	def __init__(self,get):

		self.get=get


	def create(self,user): 
		db=self.get.cursor()
		db.execute("INSERT INTO User (User_name,password,role_number) values (?,?,?)",(user.username,user.password,user.role_number))
		self.get.commit()
	def find_all(self):
		db=self.get.cursor()
		lista=self.get.execute("SELECT * FROM User ").fetchall()
		return list(lista))
