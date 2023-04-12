from repository.user_repository import user_repository
from entities.user import User
from repository.course_repository import course_repository
class Services:


	def new_user(self,name,password,role_number):
		
		user=user_repository.create(User(name,password,role_number))
		return user
		
	def find_by_rolenumber(self,rolenumber):
		lista1=[]
		lista=course_repository.find_all_course()
		for i in lista:
			if i["Role_number"]==rolenumber:
				lista1.append(i)
		return lista1



