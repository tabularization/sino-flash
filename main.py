from tkinter import *
from tkinter import messagebox
import pandas 
import random

PINK = "#F8E8EE"
BLUE = "#374259"

class FlashcardApp:
    def __init__(self):
        self.data = self.load_data()
        self.random_word = random.choice(self.data)
        self.mandarin_word = self.random_word["Mandarin"]
        self.english_word = self.random_word["English"]
        self.flip_count = 0

        self.window = Tk()
        self.window.title("Sino Flashcards")
        self.window.config(padx=50, pady=50, bg=PINK)
        
        self.flashcard = Canvas(width=800, height=526, bg=PINK, highlightthickness=0)
        self.front_image = PhotoImage(file="images/front_flashcard.png")
        self.back_image = PhotoImage(file="images/back_flashcard.png")
        self.flashcard_image = self.flashcard.create_image(400, 263, image=self.front_image)
        self.flashcard_language = self.flashcard.create_text(400, 180, text="Mandarin", font=("Arial", 15, "italic"))
        self.flashcard_text = self.flashcard.create_text(400, 270, text=random.choice(self.data)['Mandarin'], font=("Arial", 22, "bold"))
        self.flashcard.grid(column=0, row=0, columnspan=2)
        self.flashcard.bind("<Button-1>", self.flip_flashcard)
        
        check_image = PhotoImage(file="images/check.png")
        self.correct_button = Button(image=check_image, command=self.correct, bg=PINK, highlightthickness=0, bd=0, activebackground=PINK, highlightbackground=PINK)
        self.correct_button.grid(column=1, row=1)

        wrong_image = PhotoImage(file="images/wrong.png")
        self.incorrect_button = Button(image=wrong_image, command=self.update_flashcard, bg=PINK, highlightthickness=0, bd=0, activebackground=PINK, highlightbackground=PINK)
        self.incorrect_button.grid(column=0, row=1)
        
        self.window.mainloop()

    def load_data(self):
        try:
            data = pandas.read_csv("data/unlearned_words.csv")
        except:
            data = pandas.read_csv("data/mandarin_words.csv")
        return data.to_dict(orient='records')

    def correct(self):
        self.update_flashcard()
        self.data.remove(self.random_word)
        unlearned_words = pandas.DataFrame(self.data)
        if len(unlearned_words) == 0:
            user_response = messagebox.askyesno(title="Sino Flash", message=f"You've reviewed all the words.\nDo you want to restart?")
            if user_response:
                self.data = pandas.read_csv("data/mandarin_words.csv").to_dict(orient='records')
                self.update_flashcard()
            else:
                quit()
        unlearned_words.to_csv("data/unlearned_words.csv", index=False)

    def update_flashcard(self):
        self.random_word = random.choice(self.data)
        self.mandarin_word = self.random_word['Mandarin']
        self.english_word = self.random_word['English']
        self.flashcard.itemconfig(self.flashcard_image, image=self.front_image)
        self.flashcard.itemconfig(self.flashcard_language, text="Mandarin", fill="Black")
        self.flashcard.itemconfig(self.flashcard_text, text=self.mandarin_word, fill="Black")

    def flip_flashcard(self, event):
        self.flip_count += 1
        if 150 < event.x < 635 and 100 < event.y < 415:
            if self.flip_count % 2 != 0:
                self.flashcard.itemconfig(self.flashcard_image, image=self.back_image)
                self.flashcard.itemconfig(self.flashcard_text, text=self.english_word, fill=BLUE)
                self.flashcard.itemconfig(self.flashcard_language, text="English", fill=BLUE)
            else:
                self.flashcard.itemconfig(self.flashcard_image, image=self.front_image)
                self.flashcard.itemconfig(self.flashcard_language, text="Mandarin", fill="Black")
                self.flashcard.itemconfig(self.flashcard_text, text=self.mandarin_word, fill="Black")

flashcard = FlashcardApp()