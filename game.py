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
        self.resizable(False, False)
        self.iconbitmap('./images/icon.ico')
        self.lost_game = 0

        self.frame_draw = Frame(self, width=200, height=200)
        self.frame_draw.pack()
        self.frame_draw.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("./images/avatar.png"))
        # Create a Label Widget to display the text or Image
        self.label = Label(self.frame_draw, image=self.img)
        self.label.pack()
        self.score_label = Label(self, text="SCORE")
        self.score_label.pack()
        self.score_text = Label(self, text=10)
        self.score_text.pack()

        self.question_frame = LabelFrame(self, text="Question number", padx=30, pady=20)
        self.category = Label(self, text="Category...")
        self.question = Label(self, text="Question...")
        self.category.pack()
        self.question.pack()

        self.question_frame.pack(side=RIGHT, padx=100, pady=10)

        self.answer = Text(self, width=50)
        self.answer.pack()
        self.btn_accept = Button(self, text="Guess")
        self.btn_accept["command"] = self.play_game
        self.btn_accept.pack()

        self.player_question = random.choice(list(questions.keys()))
        self.category.config(text=questions[self.player_question][0])
        self.question.config(text=questions[self.player_question][1])
        self.ans = tkinter.StringVar(value=questions[self.player_question][2])

    def play_game(self):

        if self.answer.get(1.0, "end-1c") == self.ans.get():
            self.score_text.config(text=int(self.score_text['text']) + 10)
            messagebox.showinfo("showinfo", "Your answer is correct! Well done!")

            questions.pop(self.player_question, None)
            if not questions:
                messagebox.showinfo("showinfo", "You Win!")
                player_name = simpledialog.askstring("Input", "Type your name:")
                ranking.update({player_name: self.score_text['text']})
                file = open('rating.json', 'w')
                json.dump(ranking, file, indent=4)
                file.close()
                Game.quit(self)

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
                ranking.update({player_name: self.score_text['text']})
                file = open('rating.json', 'w')
                json.dump(ranking, file, indent=4)
                file.close()
                Game.quit(self)
        if questions:
            self.player_question = random.choice(list(questions.keys()))
            self.category.config(text=questions[self.player_question][0])
            self.question.config(text=questions[self.player_question][1])
            self.ans = tkinter.StringVar(value=questions[self.player_question][2])



if __name__ == "__main__":
    app = Game()
    app.mainloop()
