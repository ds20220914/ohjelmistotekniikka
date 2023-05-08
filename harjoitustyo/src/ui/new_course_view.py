from tkinter import ttk, constants
from service.studymonitoring_services import Services
from repository.course_repository import course_repository
from entities.course import Course


class NewCourseView:
    def __init__(self, root, logout):
        self._root = root
        self.logout = logout
        self._frame = None
        self.rolenumber_entry = None
        self.grade_entry = None
        self.credit_entry = None
        self.course_name_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def check_course(self):
        try:
            course_name = self.course_name_entry.get()
            rolenumber = self.rolenumber_entry.get()
            credit = self.credit_entry.get()
            grade = self.grade_entry.get()
            course = Course(course_name, credit, grade)
            result=Services()
            result1=result.add_new_course(rolenumber, course)
            print(result1)
            print(course_name,rolenumber,grade,credit)
            if result1 == False:
                error_label = ttk.Label(
                    master=self._frame, text=" course information already added or missing information or wrong information")
                error_label.grid(row=6, column=0, sticky=(
                    constants.E, constants.W))
                self.rolenumber_entry.delete(0, "end")
                self.course_name_entry.delete(0, "end")
                self.grade_entry.delete(0, "end")
                self.credit_entry.delete(0, "end")
            

            if result1 == True:
                error_label = ttk.Label(
                    master=self._frame, text=" course information added")
                error_label.grid(row=6, column=0, sticky=(
                    constants.E, constants.W))
                self.rolenumber_entry.delete(0, "end")
                self.course_name_entry.delete(0, "end")
                self.grade_entry.delete(0, "end")
                self.credit_entry.delete(0, "end")
            
        except AttributeError:
            error_label = ttk.Label(
                master=self._frame, text=" course information already added or missing information or wrong information")
            error_label.grid(row=6, column=0, sticky=(
                constants.E, constants.W))
            if self.rolenumber_entry != None:
                self.rolenumber_entry.delete(0, "end")
                
            if self.grade_entry != None:
                self.grade_entry.delete(0, "end")
                
            if self.credit_entry != None:
                self.credit_entry.delete(0, "end")
                
            if self.course_name_entry != None:
                self.course_name_entry.delete(0, "end")
                
            
            
            
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        rolenumber_label = ttk.Label(
            master=self._frame, text=" student rolenumber")
        self.rolenumber_entry = ttk.Entry(master=self._frame)
        course_name_label = ttk.Label(master=self._frame, text=" course name")
        self.course_name_entry = ttk.Entry(master=self._frame)
        grade_label = ttk.Label(master=self._frame, text="grade")
        self.grade_entry = ttk.Entry(master=self._frame)
        credit_label = ttk.Label(master=self._frame, text=" credit")
        self.credit_entry = ttk.Entry(master=self._frame)

        add = ttk.Button(
            master=self._frame, text="Add course performance", command=self.check_course)
        logout = ttk.Button(master=self._frame, text="Logout",
                            command=self.logout)

        rolenumber_label.grid(
            row=1, column=0, sticky=(constants.E, constants.W))
        self.rolenumber_entry.grid(
            row=1, column=1, sticky=(constants.E, constants.W))
        course_name_label.grid(
            row=2, column=0, sticky=(constants.E, constants.W))
        self.course_name_entry.grid(
            row=2, column=1, sticky=(constants.E, constants.W))
        grade_label.grid(row=3, column=0, sticky=(constants.E, constants.W))
        self.grade_entry.grid(
            row=3, column=1, sticky=(constants.E, constants.W))
        credit_label.grid(row=4, column=0, sticky=(constants.E, constants.W))
        self.credit_entry.grid(
            row=4, column=1, sticky=(constants.E, constants.W))
        add.grid(row=5, column=0, columnspan=2,
                 sticky=(constants.E, constants.W))
        logout.grid(row=7, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))

        self._frame.grid_columnconfigure(1, weight=1)
