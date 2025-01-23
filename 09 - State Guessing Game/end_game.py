from turtle import Turtle

FONT = ("Arial", 30, "normal")

class EndGame(Turtle):
    def __init__(self):
        super().__init__()
        self.color("maroon")
        self.penup()
        self.hideturtle()

    def win_game_writing(self):
        self.write(f"You guessed all 50 states!", align="center", font=FONT)

    def lose_game_writing(self, correct_guesses):
        self.write(f"You guessed {correct_guesses}/50 states correct.\n\n"
                   f"Please see the generated csv file\n"
                   f"to learn the states that you missed",
                   align="center", font=FONT)