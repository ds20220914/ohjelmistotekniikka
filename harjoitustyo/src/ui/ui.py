from tkinter import Tk, ttk
from ui.login_view import LoginView
from ui.teacher_view import TeacherView
from ui.student_view import StudentView
from ui.Create_user_view import Create_user
from database_connection import get_database_connection
from repository.user_repository import user_repository


class UI:
	def __init__(self,root):
		self._root=root
		self._current_view= None
		
		self._ero=None
	
	

		
	def start(self):
		self.start_login_view()

	def close_login_view(self):
		username = self._current_view.username_entry.get()
		password = self._current_view.password_entry.get()
		self._current_view.destroy()
		if username[0]=="A":
			lista=user_repository.find_all()
			for i in lista:
				if username==i["User_name"] and password==i["password"]:
					self._current_view=TeacherView(self._root)

					self._current_view.pack()
		if username[0]=="B":
			lista=user_repository.find_all()
			for i in lista:
				if username==i["User_name"] and password==i["password"]:
					self._current_view=StudentView(self._root,self.start_login_view)

					self._current_view.pack()			
		else:
			pass			


	def create_user_view(self):
		self._current_view.destroy()
		self._current_view=Create_user(self._root,self.logout)
		self._current_view.pack()
			
	def logout(self):
		self._current_view.destroy()
		self.start_login_view()
			
	def start_login_view(self):
		self._current_view=LoginView(self._root,self.close_login_view,self.create_user_view)

		self._current_view.pack()
		
	
	
		
	
		
	
		
	
	
		
	

