# Sino Flash 🀄📚

Sino Flash a simple flashcard application built using the Tkinter library in Python. It allows users to learn and review commonly used Mandarin words in flashcard format.
## Features ✨

Loads flashcard data from a CSV file (mandarin_words.csv or unlearned_words.csv).
Displays a random flashcard with a Mandarin word on the front.
Users can click on the flashcard to flip it and reveal the English translation on the back.
Provides buttons for users to indicate whether they answered correctly or incorrectly.
When a flashcard is answered correctly, it is removed from the dataset and saved in unlearned_words.csv.
If all flashcards have been reviewed, the user is prompted to restart the flashcards or quit the application.

## Prerequisites 📋

    Python 3.x
    Tkinter library
    pandas library

## How to Run ▶️

1. Make sure you have Python installed on your system.
Install the required libraries by running the following command:

        pip install pandas

2. Download the source code and navigate to the project directory.
Run the following command to start the flashcard app:

        python main.py

## Usage 🎯

1. Upon launching the app, a random flashcard will be displayed with a Mandarin word on the front.
2. Click on the flashcard to flip it and reveal the English translation on the back.
3. Click the ✅ check button if your answer is correct. The flashcard will be removed from the dataset and saved in unlearned_words.csv.
4. Click the ❌ wrong button if your answer is incorrect. The flashcard will be updated to the next random word.
5. If all flashcards have been reviewed, you will be prompted to restart or quit the application.


## Notes 📝
If the unlearned_words.csv file is not found, the app will fall back to using the mandarin_words.csv file as the data source.
The app uses the pandas library to load and manipulate the flashcard data.
The GUI is built using the tkinter library.

Note: This README assumes familiarity with the Python programming language and the Tkinter library. If you're new to Tkinter, you may want to refer to the official documentation for more information on how to use Tkinter and create GUI applications in Python.
