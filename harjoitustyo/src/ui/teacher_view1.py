from tkinter import ttk, constants
from service.studymonitoring_services import Services


class TeacherView1:
    ''' Opettajan tietyn opiskelijan suorituksen tarkistamisesta
        vastaava näkymä
    '''
    def __init__(self, root, oikea, number, logout,delete):
        ''' Luokan konstruktori. Luo uuden kurssisuorituksen tarkistusnäkymä
            Args:
                 root:
                     TKinter-elementti, jonka sisään näkymä alustetaan.
                 logout:
                     Kutsuttava arvo, joka kutsutaan kun käyttäjä haluaa kirjautua ulos
                 oikea:
                     arvo, joka kertoo onko tarkistuksen kohteena olevalla opiskelijalla
                     yhtään kurssisuoritusta.
                 delete:
                     Kutsuttava arvo, joka kutsutaan kun haluaa poistaa tietty kurssisuoritus tietyltä 
                     opiskelijalta. 
        '''
        self._root = root
        self.oikea = oikea
        self.number = number
        self.delete=delete
        self._frame = None
        self.rolenumber_entry = None
        self.delete_entry=None
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
        logout = ttk.Button(master=self._frame, text="Logout",
                            command=self.logout)
        
        if self.oikea == False:
            course_label = ttk.Label(
                master=self._frame, text="No course added")
            course_label.grid(row=1, column=0, sticky=(
                constants.E, constants.W))
            logout.grid(row=2, column=0, columnspan=2,
                        sticky=(constants.E, constants.W))

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
                logout.grid(row=len(array1)+2, column=0, columnspan=2,
                            sticky=(constants.E, constants.W))
            delete=ttk.Button(master=self._frame, text="delete by course_name",command=self.delete)
            self.delete_entry=ttk.Entry(master=self._frame)
            delete.grid(row=len(array1)+3, column=1, sticky=(
                constants.E, constants.W))
            self.delete_entry.grid(row=len(array1)+3, column=0, sticky=(
                constants.E, constants.W))

        self._frame.grid_columnconfigure(1, weight=1)
