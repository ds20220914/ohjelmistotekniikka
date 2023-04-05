from tkinter import Tk, ttk
from ui.login_view import LoginView


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
		print(username)
	def start_login_view(self):
		self._current_view=LoginView(self._root,self.close_login_view)

		self._current_view.pack()

