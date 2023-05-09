from tkinter import Tk
from ui.ui import UI


def main():
    ''' antaa ohjelmalle nimi. 
        käynnistää käyttöliittymä kun ohjelma käynnistetään
    '''
    show = Tk()
    show.title("OpS application")

    ui_show = UI(show)
    ui_show.start()

    show.mainloop()


if __name__ == "__main__":
    main()
