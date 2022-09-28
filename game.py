from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox


class Game(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('New Game')

        self.geometry('700x500')
        self.resizable(False, False)

        self.type_user_name = simpledialog.askstring("Register", "Type your name")

        if self.type_user_name == "":
            messagebox.showerror('Python Error', 'Error: This is an Error Message!')
