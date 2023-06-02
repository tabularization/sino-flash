FlashcardApp

The FlashcardApp is a simple flashcard application built using Python's Tkinter library. It allows you to learn most commonly used Mandarin words and their English translations through interactive flashcards. 🀄📚
Requirements

    Python 3.x
    Tkinter library
    Pandas library

Usage

    Install Required Libraries 🛠️

    Make sure you have the necessary libraries installed by running the following command:

pip install pandas

Prepare Data and Images 📂🖼️

    Create a directory structure as follows:

    kotlin

├── flashcard_app.py
└── data
    ├── unlearned_words.csv
    └── mandarin_words.csv

The data directory should contain two CSV files: unlearned_words.csv and mandarin_words.csv.
Place the front and back images of the flashcards in an images directory located alongside the Python file:

    ├── flashcard_app.py
    └── images
        ├── front.png
        └── back.png

Run the Flashcard Application 🚀

Open a terminal or command prompt, navigate to the directory where the Python file is located, and run the following command:

    python flashcard_app.py

    Start Learning Mandarin! 🏮🌟
        The flashcard application window will appear, displaying a randomly selected Mandarin word.
        Click on the flashcard to flip it and reveal the English translation.
        If you guessed correctly, click the ✅ button. The word will be marked as learned, and a new flashcard will appear.
        If you need more practice or guessed incorrectly, click the ❌ button. The flashcard will be replaced with a new one.
        The application automatically saves your progress, so you won't see the same word again if you clicked ✅.

That's it! Enjoy learning Mandarin with the FlashcardApp. 🀄📚
