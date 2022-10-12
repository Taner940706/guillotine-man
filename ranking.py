import json
import tkinter as tk
from tkinter import *

g = open('rating.json')
ranking = json.load(g)


class Ranking(tk.Toplevel):

	def __init__(self):
		super().__init__()
		self.title('Ranking')
		self.geometry('700x500')
		self.resizable(False, False)
		order = dict(sorted(ranking.items(), key=lambda item: -int(item[1])))
		for i in order:
			self.label = Label(self, text=f'Name: {i}; Points: {order[i]}')
			self.label.pack()
		self.btn_close = Button(self, text="Close")
		self.btn_close["command"] = self.destroy
		self.btn_close.pack()


if __name__ == "__main__":
	app = Ranking()
	app.mainloop()

