from tkinter import *
import tkinter as tk
from tkinter import ttk


class Ranking(tk.Toplevel):

	def __init__(self):
		super().__init__()
		self.title('Ranking')
		self.geometry('700x500')
		self.resizable(False, False)


if __name__ == "__main__":
	app = Ranking()
	app.mainloop()
