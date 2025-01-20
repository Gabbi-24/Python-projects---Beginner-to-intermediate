from turtle import Turtle

# Constants
START_POSITIONS_PLAYER1 = [(-752, 40), (-752, 20), (-752, 0), (-752, -20), (-752, -40)]
START_POSITIONS_PLAYER2 = [(743, 40), (743, 20), (743, 0), (743, -20), (743, -40)]
MOVE_DISTANCE = 20
HEADING_UP = 90
HEADING_DOWN = 270

class Paddle:

    def __init__(self):
        self.paddle = []
        self.paddle_head = None
        self.paddle_tail = None
        self.is_paddle_moving_up = None
        self.is_paddle_moving_down = None


    def create_paddle_player1(self):
        for position in START_POSITIONS_PLAYER1:
            paddle_segment = Turtle(shape="square")
            paddle_segment.color("white")
            paddle_segment.penup()
            paddle_segment.goto(position)
            paddle_segment.speed("fastest")
            self.paddle.append(paddle_segment)

        self.paddle_head = self.paddle[0]
        self.paddle_tail = self.paddle[-1]


    def create_paddle_player2(self):
        for position in START_POSITIONS_PLAYER2:
            paddle_segment = Turtle(shape="square")
            paddle_segment.color("white")
            paddle_segment.penup()
            paddle_segment.goto(position)
            self.paddle.append(paddle_segment)

        self.paddle_head = self.paddle[0]
        self.paddle_tail = self.paddle[-1]

    # Define these methods to use for the onkey stuff
    #-- You need a method that is true and one that is false to allow to to start and stop the paddle
    def move_paddle_up(self):
        self.is_paddle_moving_up = True

    def stop_paddle_up(self):
        self.is_paddle_moving_up = False

    def move_paddle_down(self):
        self.is_paddle_moving_down = True

    def stop_paddle_down(self):
        self.is_paddle_moving_down = False


    # Now define the method that will actually move the paddle
    #-- Use this method in the main while loop that continuously check if the method of is_moving_up or down is being called
    def move(self):
        if self.is_paddle_moving_up:
            if self.paddle_head.ycor() + MOVE_DISTANCE <= 400:  # Checks to see if the movement won't take the block off the screen
                for block_position in range(len(self.paddle)-1, 0, -1):    # Make the top the leader
                    prev_block_pos = self.paddle[block_position -1].position()
                    self.paddle[block_position].goto(prev_block_pos)

                self.paddle_head.setheading(HEADING_UP)
                self.paddle_head.forward(MOVE_DISTANCE)

        if self.paddle_head.ycor() > 400:
            self.paddle_head.sety(400)
            self.is_paddle_moving_up = False


        if self.is_paddle_moving_down:
            if self.paddle_tail.ycor() - MOVE_DISTANCE >= -380:
                for block_position in range(0, len(self.paddle) -1, 1):     # Make bottom the leader
                    next_block_pos = self.paddle[block_position + 1].position()
                    self.paddle[block_position].goto(next_block_pos)

                self.paddle_tail.setheading(HEADING_DOWN)
                self.paddle_tail.forward(MOVE_DISTANCE)

        if self.paddle_tail.ycor() < -380:
            self.paddle_tail.sety(-380)
            self.is_paddle_moving_down = False



