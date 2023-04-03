from tkinter import Tk
from ui.ui import UI

def main():
	show=TK()
	show.title("OpS application")

	ui_show=UI(show)
	ui_show.start()

	show.mainloop()
