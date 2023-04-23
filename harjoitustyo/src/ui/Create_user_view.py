from tkinter import ttk, constants
from service.studymonitoring_services import Services
from entities.user import User
from repository.user_repository import user_repository
from database_connection import get_database_connection


class Create_user:
    def __init__(self, root, start_login_view):
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
        username = self.username_entry.get()
        password = self.password_entry.get()
        studentnumber = self.number_entry.get()
        if len(username) == 0 or len(password) == 0 or studentnumber == 0:
            self._error("creation error ")
            return

        lista = user_repository.find_all()
        for i in lista:
            if username in i:
                self._error("creation error,try other username")
                return
        käyttäjä = User(username, password, studentnumber)
        uusi = Services()
        uusi.new_user(username, password, studentnumber)
        self._start_login_view()

    def _error(self, message):
        self._error_label = ttk.Label(master=self._frame, text=message)
        self._error_label.grid(
            row=6, column=0, sticky=(constants.E, constants.W))

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
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
        last_label.grid(row=5, column=0, sticky=(constants.E, constants.W))
        self._frame.grid_columnconfigure(1, weight=1)
