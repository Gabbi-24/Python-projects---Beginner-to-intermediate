from turtle import Turtle, Screen

MOVE_DISTANCE = 10

class Snake:
    screen = Screen()
    # -- Prevent screen from autoupdating the image
    screen.tracer(0)

    def __init__(self):
        self.snake_block_list = []
        self.starting_x_coord = 0
        self.create_snake()
        self.head_of_snake = self.snake_block_list[0]

    def create_snake(self):
        for index in range(3):
            snake_block = Turtle(shape="square")
            snake_block.penup()
            snake_block.speed("slow")
            self.snake_block_list.append(snake_block)
            snake_block.color("white")
            snake_block.goto(x=self.starting_x_coord, y=0)
            self.starting_x_coord -= 20

        Snake.screen.update()   # Control when screen updates


    def move(self):
        for segment_number in range(len(self.snake_block_list) - 1, 0, -1):  # Loop through list in reverse
            x_coord = self.snake_block_list[segment_number - 1].xcor()
            y_coord = self.snake_block_list[segment_number - 1].ycor()
            seg_position = (x_coord, y_coord)  # Get the last block to move to pos of block in front of it
            self.snake_block_list[segment_number].goto(seg_position)

        self.head_of_snake.forward(MOVE_DISTANCE)  # Move the first block forward


    def head_up(self):
        if self.head_of_snake.heading() != 270:
            self.head_of_snake.setheading(90)


    def head_down(self):
        if self.head_of_snake.heading() != 90:
            self.snake_block_list[0].setheading(270)


    def head_left(self):
        if self.head_of_snake.heading() != 0:
            self.head_of_snake.setheading(180)


    def head_right(self):
        if self.head_of_snake.heading() != 180:
            self.head_of_snake.setheading(0)


    def create_tail_segment(self):
        snake_block = Turtle(shape="square")
        snake_block.penup()
        snake_block.speed("fastest")

        last_seg_position = self.snake_block_list[-1]
        snake_block.goto(last_seg_position.xcor(), last_seg_position.ycor())
        snake_block.color("white")

        self.snake_block_list.append(snake_block)



