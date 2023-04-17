from tkinter import ttk, constants
from service.studyMonitoring_services import Services


class TeacherView1:
    def __init__(self, root, oikea, number):
        self._root = root
        self.oikea = oikea
        self.number = number
        self._frame = None
        self.rolenumber_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        if self.oikea == False:
            course_label = ttk.Label(
                master=self._frame, text="No course added")
            course_label.grid(row=1, column=0, sticky=(
                constants.E, constants.W))

        if self.oikea == True:
            array = Services()
            array1 = array.find_by_rolenumber(self.number)
            for i in range(len(array1)):
                course_label = ttk.Label(master=self._frame, text=array1[i])
                course_label.grid(row=i+1, column=0,
                                  sticky=(constants.E, constants.W))

        self._frame.grid_columnconfigure(1, weight=1)
