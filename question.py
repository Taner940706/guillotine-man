from tkinter import ttk
import tkinter as tk
from tkinter import *


class Question(tk.Toplevel):

	def __init__(self):
		super().__init__()
		self.title('Question')
		self.geometry('700x500')
		self.resizable(False, False)

		self.main_label = Label(self, text = "Create New Question")
		self.main_label.pack()
		self.category_label = Label(self, text = "Select Category")
		self.main_label.pack()
		self.variable = StringVar()
		self.variable.set(self.countries[3])
		self.dropdown = OptionMenu(self,self.variable,*self.countries,command=self.display_selected)
		self.dropdown.pack(expand=True)
		self.question_text = Text(self, width = 20)
		self.question_text.pack()
		self.answer_text = Text(self, width = 20)
		self.answer_text.pack()


	def display_selected(self, choice):
		choice = self.variable.get()
		print(choice)

	# for test
	countries = ['Bahamas','Canada', 'Cuba','United States']


if __name__ == "__main__":
	app = Question()
	app.mainloop()