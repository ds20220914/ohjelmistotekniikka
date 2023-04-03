from tkinter import ttk, constants		
class LoginView:
	def __init__(self,root,close_login_view):
		self._root=root
		self._close_login_view=close_login_view
		self._frame=None
		self._initialize()


	def pack(self):
		self._frame.pack(fill=constants.X)

	def destroy(self):
		self._frame.destroy()

	def _initialize(self):
		self._frame=ttk.Frame(master=self._root)
		heading= ttk.Label(master=self._root, text="welcome")
		username_label=ttk.Label(master=self._root,text="Username")
		username_entry=ttk.Entry(master=self._root)
		password_label = ttk.Label(master=self._root, text="Password")
		password_entry = ttk.Entry(master=self._root)

		login = ttk.Button(master=self._root, text="Login",command=self._close_login_view)
		username_label.grid(row=1, column=0)
		username_entry.grid(row=1, column=1)

		password_label.grid(row=2, column=0)
		password_entry.grid(row=2, column=1)
		button.grid(row=3, column=0, columnspan=2)
