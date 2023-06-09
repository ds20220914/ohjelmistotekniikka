from tkinter import ttk, constants


class LoginView:
    '''Käyttäjän kirjautumisesta vastaava näkymä.'''
    def __init__(self, root, close_login_view, create_user_view, right):
        """Luokan konstruktori. Luo uuden kirjautumisnäkymän.
           Args:
                root:
                    TKinter-elementti, jonka sisään näkymä alustetaan.
                close_login_view:
                    Kutsuttava arvo, joka kutsutaan kun käyttäjä kirjautuu sisään
                create_user_view:
                    Kutsuttava arvo, joka kutsutaan kun käyttäjä siirrytään uuden 
                    käyttäjän luomisnäkymään.
                right:
                    Joko False tai True, jos on False niin esitää virheilmoitus. 
        """
        
        self._root = root
        self._close_login_view = close_login_view
        self._create_user_view = create_user_view
        self.right = right
        self._frame = None
        self.username_entry = None
        self.password_entry = None

        self._initialize()

    def pack(self):
        '''Näyttää näkymän'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Tuhoaa näkymän'''
        self._frame.destroy()

    def _initialize(self):
        ''' määrittää sisäänkirjautumisnäkymän toiminta ja ulkoasu
        '''
        self._frame = ttk.Frame(master=self._root)
        heading = ttk.Label(master=self._frame, text="welcome")
        username_label = ttk.Label(master=self._frame, text="Username")

        self.username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Password")
        self.password_entry = ttk.Entry(master=self._frame)

        Login = ttk.Button(master=self._frame, text="Login",
                           command=self._close_login_view)
        create = ttk.Button(master=self._frame, text="Register",
                            command=self._create_user_view)
        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W))
        self.username_entry.grid(
            row=1, column=1, sticky=(constants.E, constants.W))
        password_label.grid(row=2, column=0, sticky=(constants.E, constants.W))
        self.password_entry.grid(
            row=2, column=1, sticky=(constants.E, constants.W))
        Login.grid(row=3, column=0, columnspan=2,
                   sticky=(constants.E, constants.W))
        create.grid(row=4, column=0, columnspan=2,
                    sticky=(constants.E, constants.W))
        if self.right == False:
            error_label = ttk.Label(master=self._frame, text="Login error")
            error_label.grid(row=5, column=0, sticky=(
                constants.E, constants.W))

        self._frame.grid_columnconfigure(1, weight=1)
