from tkinter import ttk, constants
	
class LoginView:
	def __init__(self,root,close_login_view):
		self._root=root
		self._close_login_view=close_login_view
		self._frame=None
		self.username_entry=None
		self.password_entry=None
		
		self._initialize()
		
	
		
	

	def pack(self):
		self._frame.pack(fill=constants.X)

	def destroy(self):
		self._frame.destroy()
		
	def _initialize(self):
		self._frame=ttk.Frame(master=self._root)
		heading= ttk.Label(master=self._frame, text="welcome")
		username_label=ttk.Label(master=self._frame,text="Username")
		
		self.username_entry=ttk.Entry(master=self._frame)
		password_label = ttk.Label(master=self._frame, text="Password")
		self.password_entry = ttk.Entry(master=self._frame)
		
		
		Login = ttk.Button(master=self._frame, text="Login",command=self._close_login_view)
		username_label.grid(row=1, column=0,sticky=(constants.E, constants.W))
		self.username_entry.grid(row=1, column=1,sticky=(constants.E, constants.W))
		password_label.grid(row=2, column=0,sticky=(constants.E, constants.W))
		self.password_entry.grid(row=2, column=1,sticky=(constants.E, constants.W))
		Login.grid(row=3, column=0, columnspan=2,sticky=(constants.E, constants.W))
		
		
		self._frame.grid_columnconfigure(1, weight=1)
		
