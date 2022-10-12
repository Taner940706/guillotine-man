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
        self.scrollbar = Scrollbar(self.frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        self.help_text = Text(self.frame, width=20)
        self.help_text.pack(padx=10, pady=10)
        self.scrollbar.config(command=self.help_text.yview)
        self.btn_close = Button(self.frame, text='Close')
        self.btn_close["command"] = self.destroy
        self.btn_close.pack()


if __name__ == "__main__":
    app = Help()
    app.mainloop()