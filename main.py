from tkinter import *

BLONDE = "#F9FBE7"
BEIGE = "#F0EDD4"
ORANGE = "#ECCDB4"
SALMON = "#FEA1A1"

# Set up window
window = Tk()
window.title("Sino Flashcards")
window.config(padx=50, pady=50, bg=ORANGE)

# Front flashcard UI
flashcard = Canvas(width=800, height=526, bg=ORANGE, highlightthickness=0)
front_image = PhotoImage(file="images/front.png")
flashcard.create_image(400, 263, image=front_image)
language = flashcard.create_text(400, 180, text="Mandarin", font=("Arial", 20, "italic"))
word = flashcard.create_text(400, 270, text="的 (de)", font=("Arial", 40, "bold"))
flashcard.grid(column=0, row=0, columnspan=2)

# Correct button
check_image = PhotoImage(file="images/check.png")
correct_button = Button(image=check_image, bg=ORANGE, highlightthickness=0, bd=0, activebackground=ORANGE, highlightbackground=ORANGE)
correct_button.grid(column=1, row=1)

# Incorrect Button
wrong_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=wrong_image, bg=ORANGE, highlightthickness=0, bd=0, activebackground=ORANGE, highlightbackground=ORANGE)
incorrect_button.grid(column=0, row=1)



window.mainloop()