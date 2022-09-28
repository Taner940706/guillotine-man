import time
import tkinter as tk
from tkinter import ttk
from game import Game
from ranking import Ranking
from about import About
from help import Help
from question import Question
from splash import SplashScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('HangMan with questions')
        self.geometry('700x500')
        self.resizable(False, False)

        #menu
        self.my_menu = tk.Menu(self)
        self.config(menu=self.my_menu)
        self.main_menu = tk.Menu(self.my_menu)
        self.my_menu.add_cascade(label="Menu", menu=self.main_menu)
        self.main_menu.add_command(label="New Game", command=Game)
        self.main_menu.add_command(label="Add Question", command=Question)
        self.main_menu.add_command(label="Ranking", command=Ranking)
        self.main_menu.add_command(label="About", command=About)
        self.main_menu.add_command(label="Help", command=Help)
        self.main_menu.add_separator()
        self.main_menu.add_command(label="Exit", command=self.quit)


if __name__ == "__main__":
    splash = SplashScreen()
    splash.after(3000, splash.destroy)
    splash.mainloop()
    app = App()
    app.mainloop()
