from turtle import Screen
import time
from snake import Snake

##### Screen setup #####
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


##### Create snake #####
snake = Snake()


##### Listen for input and assign keys #####
screen.listen()
screen.onkey(fun=snake.head_up, key="Up")
screen.onkey(fun=snake.head_down, key="Down")
screen.onkey(fun=snake.head_left, key="Left")
screen.onkey(fun=snake.head_right, key="Right")


##### Move the snake #####
game_over = False

while not game_over:
    screen.update()  # Controlling when the animation is updated
    time.sleep(0.1)   # Control the speed of the updates

    snake.move()




##### Get screen to stay on #####
screen.exitonclick()