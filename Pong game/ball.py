from turtle import Turtle, Screen
import random
import time

MOVE_DISTANCE = 10
START_HEAD_CHOICES = [45, 135, 225, 315]

screen = Screen()

class Ball(Turtle):

    def __init__(self, difficulty):
        super().__init__()
        self.color("orchid1")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.setheading(random.choice(START_HEAD_CHOICES))
        if difficulty == "1":     # Set starting speed of ball
            self.move_speed = 0.08
        elif difficulty == "2":
            self.move_speed = 0.05
        elif difficulty == "3":
            self.move_speed = 0.02


    def random_heading_left(self, player2):   # Take into account the movement of player 2's paddle
        if player2.is_paddle_moving_up:
            self.setheading(random.randint(100, 170))
        elif player2.is_paddle_moving_down:
            self.setheading(random.randint(190, 260))
        elif 10 <= self.heading() <= 80:
            self.setheading(random.randint(100, 170))
        elif 280 <= self.heading() <= 350:
            self.setheading(random.randint(190, 260))
        else:
            self.setheading(random.randint(100, 260))


    def random_heading_right(self, player1):    # Take into account the movement of player 1's paddle
        if player1.is_paddle_moving_up:
            self.setheading(random.randint(10, 80))
        elif player1.is_paddle_moving_down:
            self.setheading(random.randint(280, 350))
        elif 100 <= self.heading() <= 170:
            self.setheading(random.randint(10, 80))
        elif 190 <= self.heading() <= 260:
            self.setheading(random.randint(280, 350))
        else:
            self.setheading(random.randint(10, 80) and random.randint(280, 350))


    def move_ball(self):
        self.forward(MOVE_DISTANCE)