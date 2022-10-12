import tkinter as tk
from tkinter import *
import json

f = open('questions.json')
questions = json.load(f)


class Question(tk.Toplevel):

	def __init__(self):
		super().__init__()
		self.title('Question')
		self.geometry('700x500')
		self.resizable(False, False)


		self.main_label = Label(self, text="Create New Question")
		self.main_label.pack()
		self.category_label = Label(self, text="Select Category")
		self.main_label.pack()
		self.category = Entry(self, width=20)
		self.category.pack(padx=10, pady=10)
		self.question_text = Entry(self, width=20)
		self.question_text.pack(padx=10, pady=10)
		self.answer_text = Entry(self, width=20)
		self.answer_text.pack(padx=10, pady=10)
		self.btn_accept = Button(self, text="Add Question")
		self.btn_accept["command"] = self.add_question
		self.btn_accept.pack()
		self.btn_close = Button(self, text="Close")
		self.btn_close["command"] = self.destroy
		self.btn_close.pack()

	def add_question(self):
		questions.update({str(len(questions)+1): [self.category.get(), self.question_text.get(), self.answer_text.get()]})
		file = open('questions.json', 'w')
		json.dump(questions, file, indent=4)
		file.close()


if __name__ == "__main__":
	app = Question()
	app.mainloop()
