from tkinter import ttk, constants
	
class StudentView:
	def __init__(self,root,logout):
		self._root=root
		self._logout=logout
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
		Keskiarvo_label=ttk.Label(master=self._frame,text="Keskiarvo:")
		Opintopiste_label=ttk.Label(master=self._frame,text="Opintopisteet:")
		Kurssinimi_label=ttk.Label(master=self._frame,text="Kurssinimi")
		Arvosana_label=ttk.Label(master=self._frame,text="Arvosana")
		Opintopiste1_label=ttk.Label(master=self._frame,text="Opintopiste")
		
		
		Logout = ttk.Button(master=self._frame, text="Logout",command=self._logout)
		Keskiarvo_label.grid(row=1, column=0,sticky=(constants.E, constants.W))
		Opintopiste_label.grid(row=2, column=0,sticky=(constants.E, constants.W))
		Kurssinimi_label.grid(row=3, column=0,sticky=(constants.E, constants.W))
		Arvosana_label.grid(row=3, column=5,sticky=(constants.E, constants.W))
		Opintopiste1_label.grid(row=3, column=13,sticky=(constants.E, constants.W))
		
		
		Logout.grid(row=4, column=0, columnspan=2,sticky=(constants.E, constants.W))
		
		
		self._frame.grid_columnconfigure(1, weight=1)
