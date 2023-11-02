from tkinter import Tk, Label, Button, PhotoImage
from PIL import Image, ImageTk
import random

class Game:
    def __init__(self, country_collection):
        self.country_collection = country_collection
        self.current_country = None
        self.score = 0

        # Create the main window
        self.window = Tk()
        self.window.title("Fun with Flags")

        # Add a label for the score
        self.score_label = Label(self.window, text=f"Score: {self.score}")
        self.score_label.pack()

        # Add a label to display the flag image
        self.flag_label = Label(self.window)
        self.flag_label.pack()

        # Add buttons for the multiple choice answers
        self.buttons = [Button(self.window) for _ in range(4)]
        for button in self.buttons:
            button.pack()

        # Start the game
        self.start_game()

        # Start the main event loop
        self.window.mainloop()

    def start_game(self):
        self.current_country = self.country_collection.get_random_country()

        # Update the flag image
        image = Image.open(self.current_country.image_path)
        photo = ImageTk.PhotoImage(image)
        self.flag_label.configure(image=photo)
        self.flag_label.image = photo  # keep a reference to the image

        # Update the multiple choice buttons
        correct_answer = self.current_country.name

        all_names = [country.name for country in self.country_collection.countries]
        all_names.remove(correct_answer)

        wrong_answers = random.sample(all_names, 3)
        answers = [correct_answer] + wrong_answers
        random.shuffle(answers)
        for button, answer in zip(self.buttons, answers):
            button.configure(text=answer, command=lambda ans=answer: self.check_answer(ans))

    # the rest of your Game class...
    # check answer class
    def check_answer(self, answer):
        if answer == self.current_country.name:
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")
        else:
            self.score = 0
            self.score_label.configure(text=f"Score: {self.score}")
        self.start_game()
