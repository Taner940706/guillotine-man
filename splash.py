from tkinter import ttk
import tkinter as tk
from tkinter import *
import time


class SplashScreen(tk.Tk):

    def __init__(self):
        super().__init__()
        self.img = PhotoImage(file="./images/splash.png")
        self.label = Label(self,image=self.img)
        self.label.place(x=0, y=0)
        self.wm_attributes('-fullscreen', 'True')
