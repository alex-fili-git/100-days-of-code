from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
try:
    to_learn = pd.read_csv("words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    to_learn = pd.read_csv("es_en.csv").to_dict(orient="records")

word = None

def update():
    global word, to_learn
    to_learn.remove(word)
    pd.DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)

def turn():
    global word
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")
    canvas.itemconfig(background, image=card_back_img)


def new_random_word():
    global word, timer
    word = choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=word["French"], fill="black")
    canvas.itemconfig(background, image=card_front_img)
    try:
        window.after_cancel(timer)
    except:
        pass
    timer = window.after(3000, func=turn)



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# UI front of card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Language", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="Start with X", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=lambda: [new_random_word(), update()])
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_random_word)
wrong_button.grid(column=0, row=1)


window.mainloop()
