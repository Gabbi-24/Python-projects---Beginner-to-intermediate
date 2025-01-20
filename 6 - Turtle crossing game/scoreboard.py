from turtle import Turtle

from car_manager import CarManager
from player import Player
FONT = ("Courier", 24, "normal")
FONT_END = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("Black")
        self.level_number = 1
        self.goto(-280,260)

    def level_text(self):
        self.increase_level()
        self.clear()
        self.write(f"Level {self.level_number}", align="left", font=FONT)

    def increase_level(self):
        if Player.restarted:
            self.level_number += 1

    def game_ends(self):
        if CarManager.collision:
            self.home()
            self.write(f"GAME OVER", align="center", font=FONT_END)