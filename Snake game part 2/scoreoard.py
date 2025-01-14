from turtle import Turtle

FONT_SCORE = ("Arial", 16, "normal")
FONT_GAME_OVER = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0


    def display_score(self):
        self.goto(0, 270)
        self.clear()
        score_heading = f"Your current score: {self.score}"
        self.write(score_heading, move=False, align="center", font=FONT_SCORE)


    def update_score(self):
        self.score += 1


    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.color("maroon1")
        game_over_text = f"Game Over! Your final score is: {self.score}"
        self.write(game_over_text, move=False, align="center", font=FONT_GAME_OVER)