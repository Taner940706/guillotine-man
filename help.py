import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


class Help(tk.Toplevel):
    def __init__(self,):
        super().__init__()
        self.title('Help')
        self.geometry('700x500')
        self.resizable(False, False)
        self.iconbitmap('./images/icon.ico')
        self.frame = Frame(self, width=200, height=200)
        self.frame.pack()

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("./images/avatar.png"))

    # Create a Label Widget to display the text or Image
        self.label = Label(self.frame, image=self.img)
        self.label.pack()
        self.help_text = Label(self.frame, width=20, text="Game:\n Category text field: Category of the question.\n Question text field: question, who the player can find the answer.\n Score text field: score of the current player. \n Answer text field: the player answer for the current question.\n Guess button: button for checking the player answer.\n Question Form:/n Category text field: add category to the question.\n Question text field: add question.\n Answer text field: add answer.\n Ranking Form: \n For every registration, player result (score) is added the the ranking list and order by all score descending.\n About: \n Information about software and useful links.\n Help:\n Information about components and usage.")
        self.help_text.pack(padx=10, pady=10)
        self.btn_close = Button(self.frame, text='Close')
        self.btn_close["command"] = self.destroy
        self.btn_close.pack()


if __name__ == "__main__":
    app = Help()
    app.mainloop()