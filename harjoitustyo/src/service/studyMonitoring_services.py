from repository.user_repository import user_repository
from entities.user import User
from repository.course_repository import course_repository
class Services:


	def new_user(self,name,password,role_number):
		
		user=user_repository.create(User(name,password,role_number))
		return user
		
	def find_by_rolenumber(self,rolenumber):

		lista=course_repository.find_all_course_by_Student_role_number(rolenumber)
		
		return lista
		
	def find_by_coursename_rolenumber(self,rolenumber,course_name):
		lista=course_repository.find_all_course_by_Student_role_number(rolenumber)
		for i in lista:
			if course_name==i["Course_name"]:
				return False
		return True
		
			
	


