from tkinter import ttk, constants
from service.studymonitoring_services import Services
from entities.user import User
from repository.user_repository import user_repository
from database_connection import get_database_connection


class Create_user:
    ''' Uuden käyttäjän luomisesta vastaava näkymä
    '''
    def __init__(self, root, start_login_view):
        ''' Luokan konstruktori. Luo uuden kurssisuorituksen lisäämisnäkymän
            Args:
                 root:
                     TKinter-elementti, jonka sisään näkymä alustetaan.
                 start_login_view:
                     kutsuttava arvo, joka kutsutaan kun uuden käyttäjän luominen onnistuu
                     tai jos käyttäjä haluaa mene takaisin kirjautumisnäkymään
        '''
        self._root = root
        self._start_login_view = start_login_view
        self._frame = None
        self.username_entry = None
        self.password_entry = None
        self.number_entry = None
        self._error_variable = None
        self._error_label = None
        self._initialize()

    def check_create_user(self):
        ''' luo uusi käyttäjä ja tarkistaa onnistuuko uuden käyttäjän luominen'''
        username = self.username_entry.get()
        password = self.password_entry.get()
        studentnumber = self.number_entry.get()
        user = User(username, password, studentnumber)
        new = Services()
        result=new.new_user(user.username, user.password, user.role_number)
        if result==False:
            self._error("creation error,try other username or rolenumber already have")
            return
        if result==True:
            self._start_login_view()

    def _error(self, message):
        ''' antaa virhe ilmoitus'''
        self._error_label = ttk.Label(master=self._frame, text=message)
        self._error_label.grid(
            row=7, column=0, sticky=(constants.E, constants.W))

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
        username_label = ttk.Label(master=self._frame, text="Create username")

        self.username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Create password")
        self.password_entry = ttk.Entry(master=self._frame)
        number_label = ttk.Label(master=self._frame, text="Your role number")
        self.number_entry = ttk.Entry(master=self._frame)

        create = ttk.Button(master=self._frame, text="Register",
                            command=self.check_create_user)
        back1=ttk.Button(master=self._frame, text="Go back",
                            command=self._start_login_view)
        last_label = ttk.Label(
            master=self._frame, text="The first alphabet of the username has to be B if you are student, A if you are teacher.")

        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W))
        self.username_entry.grid(
            row=1, column=1, sticky=(constants.E, constants.W))
        password_label.grid(row=2, column=0, sticky=(constants.E, constants.W))
        self.password_entry.grid(
            row=2, column=1, sticky=(constants.E, constants.W))
        number_label.grid(row=3, column=0, sticky=(constants.E, constants.W))
        self.number_entry.grid(
            row=3, column=1, sticky=(constants.E, constants.W))
        create.grid(row=4, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))
        back1.grid(row=5, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))
        last_label.grid(row=6, column=0, sticky=(constants.E, constants.W))
        self._frame.grid_columnconfigure(1, weight=1)
