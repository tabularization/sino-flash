from tkinter import *
import pandas 
import random

BLONDE = "#F9FBE7"
BEIGE = "#F0EDD4"
ORANGE = "#ECCDB4"
SALMON = "#FEA1A1"
RANDOM_WORD = ""
MANDARIN_WORD = ""
ENGLISH_WORD = ""

# Reading data
data = pandas.read_csv("data/mandarin_words.csv")
data = data.to_dict(orient='records')
RANDOM_WORD = random.choice(data) # Not the best way to do this

# ---------------------------- FUNCTIONS ------------------------------- #
def correct():
    global MANDARIN_WORD
    update_flashcard()
    print(MANDARIN_WORD)
     
def update_flashcard():
    global MANDARIN_WORD
    global RANDOM_WORD
    flashcard.itemconfig(flashcard_image, image=front_image)
    flashcard.itemconfig(flashcard_language, text="Mandarin", fill="Black")
    RANDOM_WORD = random.choice(data)
    MANDARIN_WORD = RANDOM_WORD['Mandarin']
    flashcard.itemconfig(flashcard_text, text=MANDARIN_WORD, fill="Black")

def flip_flashcard(event):
    global ENGLISH_WORD
    ENGLISH_WORD = RANDOM_WORD['English']       
    if 150 < event.x < 635 and 100 < event.y < 415:
        flashcard.itemconfig(flashcard_image, image=back_image)
        flashcard.itemconfig(flashcard_text, text=ENGLISH_WORD, fill="White")
        flashcard.itemconfig(flashcard_language, text="English", fill="White")
 
# ---------------------------- UI SETUP ------------------------------- #
# Set up window
window = Tk()
window.title("Sino Flashcards")
window.config(padx=50, pady=50, bg=ORANGE)

# Front flashcard UI
flashcard = Canvas(width=800, height=526, bg=ORANGE, highlightthickness=0)
front_image = PhotoImage(file="images/front.png")
back_image = PhotoImage(file="images/back.png")
flashcard_image = flashcard.create_image(400, 263, image=front_image)
flashcard_language = flashcard.create_text(400, 180, text="Mandarin", font=("Arial", 15, "italic"))
flashcard_text = flashcard.create_text(400, 270, text=random.choice(data)['Mandarin'], font=("Arial", 22, "bold"))
flashcard.grid(column=0, row=0, columnspan=2)
flashcard.bind("<Button-1>", flip_flashcard)
# Correct button
check_image = PhotoImage(file="images/check.png")
correct_button = Button(image=check_image, command=correct, bg=ORANGE, highlightthickness=0, bd=0, activebackground=ORANGE, highlightbackground=ORANGE)
correct_button.grid(column=1, row=1)

# Incorrect Button
wrong_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=wrong_image, command=update_flashcard, bg=ORANGE, highlightthickness=0, bd=0, activebackground=ORANGE, highlightbackground=ORANGE)
incorrect_button.grid(column=0, row=1)




window.mainloop()