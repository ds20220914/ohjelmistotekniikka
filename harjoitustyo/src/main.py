from tkinter import Tk
from ui.ui import UI


def main():
    show = Tk()
    show.title("OpS application")

    ui_show = UI(show)
    ui_show.start()

    show.mainloop()


if __name__ == "__main__":
    main()
