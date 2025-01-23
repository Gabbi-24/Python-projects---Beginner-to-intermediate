from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    restarted = False

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)

    def stop_moving(self):
        self.forward(0)
        self.backward(0)

    def check_player_position(self):
        if self.ycor() > FINISH_LINE_Y:
            Player.restarted = True
            self.goto(STARTING_POSITION)
        else:
            Player.restarted = False
