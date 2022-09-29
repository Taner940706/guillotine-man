from tkinter import ttk
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


class About(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('About')
        self.geometry('700x500')
        self.resizable(False, False)
        self.iconbitmap('./images/icon.ico')
        self.frame = Frame(self, width=200, height=200)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("./images/avatar.png"))

        # Create a Label Widget to display the text or Image
        self.label = Label(self.frame, image=self.img)
        self.label.pack()
        self.about_project_label = Label(self.frame, text="some text here")
        self.about_project_label.pack(pady=20)
        self.about_me_label = Label(self.frame, text="Created by Taner Ismail")
        self.about_me_label.pack(pady=20)
        self.btn_close = Button(self.frame, text='Close')
        self.btn_close["command"] = self.destroy
        self.btn_close.pack()


if __name__ == "__main__":
    app = About()
    app.mainloop()