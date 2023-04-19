from tkinter import ttk, constants
from service.studyMonitoring_services import Services

class StudentView:
    def __init__(self, root,logout,username):
        self._root = root
        self._logout = logout
        self._frame = None
        self.username=username
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        x=Services()
        lista=x.find_course_by_username(self.username)
        self._frame = ttk.Frame(master=self._root)
        Keskiarvo_label = ttk.Label(master=self._frame, text="Keskiarvo:")
        Opintopiste_label = ttk.Label(
            master=self._frame, text="Opintopisteet:")
        Kurssinimi_label = ttk.Label(master=self._frame, text="Kurssinimi")
        Arvosana_label = ttk.Label(master=self._frame, text="Arvosana")
        Opintopiste1_label = ttk.Label(master=self._frame, text="Opintopiste")

        Logout = ttk.Button(master=self._frame,
                            text="Logout", command=self._logout)
        Keskiarvo_label.grid(
            row=1, column=0)
        Opintopiste_label.grid(
            row=1, column=0)
        Kurssinimi_label.grid(
            row=2, column=0)
        Arvosana_label.grid(row=2, column=1)
        Opintopiste1_label.grid(
            row=2,column=2)
        
        for i in range(len(lista)):

                course_label1 = ttk.Label(
                    master=self._frame, text=lista[i]["Course_name"])
                course_label2 = ttk.Label(
                    master=self._frame, text=lista[i]["grade"])
                course_label3 = ttk.Label(
                    master=self._frame, text=lista[i]["Credit"])
                course_label1.grid(row=i+3, column=0)

                course_label2.grid(row=i+3, column=1)

                course_label3.grid(row=i+3, column=2)

        Logout.grid(row=len(lista)+2+1, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))

        self._frame.grid_columnconfigure(1, weight=1)
