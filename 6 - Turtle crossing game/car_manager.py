from turtle import Turtle
from player import Player
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    move_distance = STARTING_MOVE_DISTANCE
    collision = False

    def __init__(self, player_turtle):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.setposition(x=315, y=random.randint(-250,260))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.speed("slowest")
        self.player_turtle = player_turtle


    def move_car(self):
        self.forward(CarManager.move_distance)
        self.detect_collision()

    def increase_speed(self):
        CarManager.move_distance += MOVE_INCREMENT

    def detect_collision(self):
        if abs(self.xcor()-self.player_turtle.xcor()) < 20 and abs(self.ycor()-self.player_turtle.ycor()) < 20:
            CarManager.collision = True



