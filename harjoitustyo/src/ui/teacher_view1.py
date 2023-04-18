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
            course_label4 = ttk.Label(master=self._frame, text="course_name")
            course_label5 = ttk.Label(master=self._frame, text="grade")
            course_label6 = ttk.Label(master=self._frame, text="credit")
            course_label4.grid(row=1, column=0)
            course_label5.grid(row=1, column=1)
            course_label6.grid(row=1, column=2)
            for i in range(len(array1)):

                course_label1 = ttk.Label(
                    master=self._frame, text=array1[i]["Course_name"])
                course_label2 = ttk.Label(
                    master=self._frame, text=array1[i]["grade"])
                course_label3 = ttk.Label(
                    master=self._frame, text=array1[i]["Credit"])
                course_label1.grid(row=i+2, column=0)

                course_label2.grid(row=i+2, column=1)

                course_label3.grid(row=i+2, column=2)

        self._frame.grid_columnconfigure(1, weight=1)
