from tkinter import Tk, ttk
from ui.login_view import LoginView

class UI:
	def __init__(self,frame):
		self._root=root
		self._current_view= None
		
	def start(self):
		self.start_login_view()

	def close_login_view(self):
		print("bye")
	def start_login_view(self):
		self._current_view=LoginView(self._root,self.close_login_view)

		self._current_view.pack()

