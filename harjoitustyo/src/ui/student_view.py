from tkinter import ttk, constants
from service.studymonitoring_services import Services


class StudentView:
    def __init__(self, root, logout, username,diagram):
        self._root = root
        self._logout = logout
        self._frame = None
        self.username = username
        self.diagram=diagram
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        x = Services()
        lista = x.find_course_by_username(self.username)
        grade = x.average_grade(self.username)
        credit_sum = x.credit_sum(self.username)
        self._frame = ttk.Frame(master=self._root)
        average_grade_label = ttk.Label(
            master=self._frame, text="Average grade:")
        grade_label = ttk.Label(master=self._frame, text=grade)
        credit_sum_label = ttk.Label(master=self._frame, text=credit_sum)
        credit_label = ttk.Label(
            master=self._frame, text="Credits together:")
        course_name_label = ttk.Label(master=self._frame, text="course name")
        grade1_label = ttk.Label(master=self._frame, text="grade")
        credit1_label = ttk.Label(master=self._frame, text="credit")

        Logout = ttk.Button(master=self._frame,
                            text="Logout", command=self._logout)
        diagram = ttk.Button(master=self._frame,
                            text="show average grade diagram", command=self.diagram)
        average_grade_label.grid(
            row=1, column=0)
        grade_label.grid(row=1, column=1)
        credit_label.grid(
            row=2, column=0)
        credit_sum_label.grid(row=2, column=1)
        course_name_label.grid(
            row=3, column=0)
        grade1_label.grid(row=3, column=1)
        credit1_label.grid(
            row=3, column=2)

        for i in range(len(lista)):

            course_label1 = ttk.Label(
                master=self._frame, text=lista[i]["Course_name"])
            course_label2 = ttk.Label(
                master=self._frame, text=lista[i]["grade"])
            course_label3 = ttk.Label(
                master=self._frame, text=lista[i]["Credit"])
            course_label1.grid(row=i+4, column=0)

            course_label2.grid(row=i+4, column=1)

            course_label3.grid(row=i+4, column=2)

        Logout.grid(row=len(lista)+4, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))
        diagram.grid(row=len(lista)+5, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))

        self._frame.grid_columnconfigure(1, weight=1)
