import pandas
import tkinter as tk
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
# TODO: read data from csv
try:
    pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    print("data from french_word.csv")
else:
    data = pandas.read_csv("./data/words_to_learn.csv")
    print("data from words to learn")

# todo: convert dataframe into dictionary
# word_dict = {row["French"]: row["English"] for (index, row) in data.iterrows()}
# word_list = [item for item in word_dict]

to_learn = data.to_dict(orient="records")
current_card = {}


# ---------------------filp the card ------------------------------------ #

def flip_cards():
    canvas.itemconfig(card_img, image=new_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# -----------------Create random flash card -----------------------------#
# todo:  create a function to relative to button wrong or right
def next_card():
    global flip_timer
    global current_card
    try:
        window.after_cancel(flip_timer)
    except ValueError:
        pass

    """each time click button, generate a randon word to display"""
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        messagebox.showinfo(title="Congratulation!", message="You already learn all words in this list")
    else:
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_img, image=old_img)

        flip_timer = window.after(1000, flip_cards)


# --------------------update word---------------------------#
def is_known():
    # remove new word from word_data
    try:
        to_learn.remove(current_card)
    except ValueError:
        messagebox.showinfo(title="Congradulation!", message="You already learn all words in this list")
    else:
        word_to_learn = pandas.DataFrame(to_learn)
        word_to_learn.to_csv("./data/words_to_learn.csv", index=False)
        next_card()


# --------------------SETUP UI ----------------------------#

window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tk.Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
old_img = tk.PhotoImage(file="./images/card_front.png")
new_img = tk.PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(403, 266, image=old_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

known_img = tk.PhotoImage(file="./images/right.png")
known_button = tk.Button(image=known_img, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR,
                         command=is_known)
known_button.grid(column=1, row=1)

unknown_img = tk.PhotoImage(file="./images/wrong.png")
unknown_button = tk.Button(image=unknown_img, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR,
                           command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
