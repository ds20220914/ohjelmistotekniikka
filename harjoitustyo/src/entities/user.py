class User:


	def __init__(self,username,password,number):
		self.username=username
		self.password=password
		self.role_number=number
		if self.role_number[0]=="A":
			self.role="student"
		if self.role_number[0]=="B":
			self.role="teacher"
