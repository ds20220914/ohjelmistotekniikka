from tkinter import ttk, constants
from service.studyMonitoring_services import Services

class TeacherView:
	def __init__(self,root):
		self._root=root
		
		self._frame=None
		self.rolenumber_entry=None
		
		self._initialize()
	
	def pack(self):
		self._frame.pack(fill=constants.X)

	def destroy(self):
		self._frame.destroy()
		
	def _initialize(self):
		self._frame=ttk.Frame(master=self._root)
		heading= ttk.Label(master=self._frame, text="welcome")
		rolenumber_label=ttk.Label(master=self._frame,text="Search student rolenumber")
		
		self.rolenumber_entry=ttk.Entry(master=self._frame)
		
		
		
		search = ttk.Button(master=self._frame, text="Search",command=self.check_student())
		rolenumber_label.grid(row=1, column=0,sticky=(constants.E, constants.W))
		self.rolenumber_entry.grid(row=1, column=1,sticky=(constants.E, constants.W))
		
		search.grid(row=3, column=0, columnspan=2,sticky=(constants.E, constants.W))
		
		
		self._frame.grid_columnconfigure(1, weight=1)
		
	def check_student(self):
		number=self.rolenumber_entry.get()
		array=Services()
		array1=array.find_by_rolenumber(number)
		if len(array1)==0:
			print("ei")
		if len(array1)!=0:
			print("ok")
		
	
		
