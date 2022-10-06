import random
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import json
from PIL import ImageTk, Image

f = open('questions.json')
g = open('rating.json')
questions = json.load(f)
ranking = json.load(g)


class Game(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title('New Game')
        self.geometry('700x500')
       # self.resizable(False, False)
        self.iconbitmap('./images/icon.ico')
        self.lost_game = 0

        self.A = tk.IntVar()
        self.frame_draw = Frame(self, width=200, height=200)
        self.frame_draw.pack()
        self.frame_draw.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("./images/avatar.png"))
        # Create a Label Widget to display the text or Image
        self.label = Label(self.frame_draw, image=self.img)
        self.label.pack()
        self.score_label = Label(self, text="SCORE")
        self.score_label.place(relx=5.0, rely=0.0, anchor='ne')
        self.score_text = Label(self, textvariable=self.A)
        self.score_label.place(relx=1.0, rely=0.0, anchor='ne')

        self.question_frame = LabelFrame(self, text="Question number", padx=30, pady=20)
        self.category = Label(self, text="Category...")
        self.question = Label(self, text="Question...")
        self.category.pack()
        self.question.pack()

        self.question_frame.pack(side=RIGHT, padx=100, pady=10)

        self.answer = Text(self, width=50)
        self.answer.pack()
        self.btn_accept = Button(self, text="Send")
        self.btn_accept["command"] = self.play_game
        self.btn_accept.pack()

        self.player_question = random.choice(list(questions.keys()))
        self.category.config(text=questions[self.player_question][0])
        self.question.config(text=questions[self.player_question][1])

    def play_game(self):
        ans = tkinter.StringVar(name='ans', value=questions[self.player_question][2])
        if self.answer.get(1.0, "end-1c") == ans.get():
            del questions[self.player_question]
            messagebox.showinfo("showinfo", "Your answer is correct! Well done!")
            self.player_question = random.choice(list(questions.keys()))
            self.category.config(text=questions[self.player_question][0])
            self.question.config(text=questions[self.player_question][1])
            self.score_text += 10

        else:
            messagebox.showerror("showerror", "Not correct!")
            if self.lost_game == 0:
                self.img = ImageTk.PhotoImage(Image.open("./images/only_guillotine.png"))
                # Create a Label Widget to display the text or Image
                self.label = Label(self.frame_draw, image=self.img)
                self.label.pack()
                self.lost_game += 1
            elif self.lost_game == 1:
                self.img = ImageTk.PhotoImage(Image.open("./images/with_prisoner.png"))
                # Create a Label Widget to display the text or Image
                self.label = Label(self.frame_draw, image=self.img)
                self.label.pack()
                self.lost_game += 1
            elif self.lost_game == 2:
                self.img = ImageTk.PhotoImage(Image.open("./images/with_prisoner_judge.png"))
                # Create a Label Widget to display the text or Image
                self.label = Label(self.frame_draw, image=self.img)
                self.label.pack()
                self.lost_game += 1
            elif self.lost_game == 3:
                self.img = ImageTk.PhotoImage(Image.open("./images/game_over.png"))
                # Create a Label Widget to display the text or Image
                self.label = Label(self.frame_draw, image=self.img)
                self.label.pack()
                messagebox.showinfo("showinfo", "Game Over!")
                player_name = simpledialog.askstring("Input", "Type your name:")
                ranking[player_name] = self.score_text
                Game.quit(self)


if __name__ == "__main__":
    app = Game()
    app.mainloop()
