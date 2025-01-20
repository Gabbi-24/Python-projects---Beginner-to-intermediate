from turtle import Turtle

FONT_SCORE = 70
FONT_GAMEOVER_1 = 90
FONT_GAMEOVER_2 = 70

class ScoreBoard(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.setx(x_cor)
        self.sety(300)
        self.write_score()


    def write_score(self):
        self.write(f"{self.score}", align="center", font=("Haettenschweiler", FONT_SCORE, "normal"))


    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()


    def game_over(self, player):
        self.color("orchid1")
        self.setposition(0,30)
        self.write(f"GAME OVER",  align="center", font=("Haettenschweiler", FONT_GAMEOVER_1, "normal"))
        self.setposition(0, -60)
        self.write(f"{player} Wins!", align="center", font=("Haettenschweiler", FONT_GAMEOVER_2, "normal"))
