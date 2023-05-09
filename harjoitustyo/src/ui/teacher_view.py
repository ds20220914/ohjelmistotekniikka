from tkinter import ttk, constants
from service.studymonitoring_services import Services


class TeacherView:
    ''' Opettajan erilaisen tehtävän vastaava näkymän'''
    def __init__(self, root, check, add_new_course, logout):
        ''' Luokan konstruktori. Luo uuden opettajan tehtävänäkymä
            Args:
                 root:
                     TKinter-elementti, jonka sisään näkymä alustetaan.
                 logout:
                     Kutsuttava arvo, joka kutsutaan kun käyttäjä haluaa kirjautua ulos
                 check:
                     kutsuttava arvo, joka kutsutaan kun käyttäjä haluaa tarkistaa tietyn
                     opiskelijan kaikki suoritustiedot.
                 add_new_course:
                     kutsuttava arvi, joka kutsutaan kun käyttäjä haluaa lisätä tietylle opiskelijalle
                     kurssisuorituksen.
        '''
        self._root = root
        self.check_student = check
        self.add_new_course = add_new_course
        self._frame = None
        self.rolenumber_entry = None
        self.view = None
        self.logout = logout
        self._initialize()

    def pack(self):
        ''' näyttää näkymän'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        ''' Tuhoaa näkymän'''
        self._frame.destroy()

    def _initialize(self):
        ''' määrittää sisäänkirjautumisnäkymän toiminta ja ulkoasu
        '''
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
