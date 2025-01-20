from turtle import Turtle
import random

class Food(Turtle):    # Inherit from turtle to be able to use it's methods in the constructor

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # Basically half the default (which is 20x20) to get 10x10 pixels
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        self.goto(random.uniform(-280, 280), random.uniform(-280, 280))

