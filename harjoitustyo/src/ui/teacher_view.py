from tkinter import ttk, constants
from service.studymonitoring_services import Services


class TeacherView:
    def __init__(self, root, check, add_new_course, logout):
        self._root = root
        self.check_student = check
        self.add_new_course = add_new_course
        self._frame = None
        self.rolenumber_entry = None
        self.view = None
        self.logout = logout
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading = ttk.Label(master=self._frame, text="welcome")
        rolenumber_label = ttk.Label(
            master=self._frame, text="Search student rolenumber")

        self.rolenumber_entry = ttk.Entry(master=self._frame)

        new_course = ttk.Button(
            master=self._frame, text="Add new course", command=self.add_new_course)

        search = ttk.Button(master=self._frame, text="Search",
                            command=self.check_student)
        logout = ttk.Button(master=self._frame, text="Logout",
                            command=self.logout)
        rolenumber_label.grid(
            row=1, column=0, sticky=(constants.E, constants.W))
        self.rolenumber_entry.grid(
            row=1, column=1, sticky=(constants.E, constants.W))

        search.grid(row=3, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))
        new_course.grid(row=4, column=0, columnspan=2,
                        sticky=(constants.E, constants.W))
        logout.grid(row=5, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))

        self._frame.grid_columnconfigure(1, weight=1)
