from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

from PIL import ImageTk, Image


class Game(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title('New Game')
        self.geometry('700x500')
        self.resizable(False, False)
        self.iconbitmap('./images/icon.ico')

        self.frame_draw = Frame(self, width=200, height=200)
        self.frame_draw.pack()
        self.frame_draw.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("./images/avatar.png"))
        # Create a Label Widget to display the text or Image
        self.label = Label(self.frame_draw, image=self.img)
        self.label.pack()
        self.score_label = Label(self, text="SCORE")
        self.score_label.place(relx = 5.0,rely = 0.0, anchor ='ne')
        self.score_text = Label(self, text="0")
        self.score_label.place(relx=1.0, rely=0.0, anchor='ne')

        self.question_frame = LabelFrame(self, text="Question number", padx=30, pady=20)
        self.scenario = Label(self, text="Scenarion...")
        self.category = Label(self, text="Category...")
        self.question = Label(self, text="Question...")
        self.scenario.pack()
        self.category.pack()
        self.question.pack()

        self.question_frame.pack(side=RIGHT, padx=100, pady=10)

        self.answer = Text(self, width=50)
        self.btn_accept = Button(self, text="Send")
        self.btn_accept["command"] = "some func"


if __name__ == "__main__":
    app = Game()
    app.mainloop()