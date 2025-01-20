from turtle import Screen
from food import Food
from scoreoard import Scoreboard
import time
from snake import Snake

##### Screen setup #####
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


##### Create snake #####
snake = Snake()

##### Create food #####
food = Food()

##### Create scoreboard #####
score = Scoreboard()


##### Listen for input and assign keys #####
def listen_to_keys():
    screen.listen()
    screen.onkey(fun=snake.head_up, key="Up")
    screen.onkey(fun=snake.head_down, key="Down")
    screen.onkey(fun=snake.head_left, key="Left")
    screen.onkey(fun=snake.head_right, key="Right")

listen_to_keys()


##### Move the snake #####
game_over = False
score.display_score()

while not game_over:
    screen.update()  # Controlling when the animation is updated
    time.sleep(snake.game_speed)   # Control the speed of the updates
    snake.move()
    x_limit = snake.head_of_snake.xcor()
    y_limit = snake.head_of_snake.ycor()

    # Detect collision with food and move food accordingly
    if snake.head_of_snake.distance(food) < 15:
        food.move_food()
        snake.create_tail_segment()
        snake.game_speed *= 0.9

        # Display and update score
        score.update_score()
        score.display_score()

    # Detect collision with walls
    if snake.head_of_snake.heading() == 0 or snake.head_of_snake.heading() == 180:
        if x_limit < -290 or x_limit > 287:
            score.reset_score()
            snake.reset_snake()
            score.continue_playing()
            if Scoreboard.game_on:
                listen_to_keys()
            else:
                game_over = True
                score.reset_high_score()
                score.thanks_for_playing()

    elif snake.head_of_snake.heading() == 90 or snake.head_of_snake.heading() == 270:
        if y_limit < -287 or y_limit > 290:
            score.reset_score()
            snake.reset_snake()
            score.continue_playing()
            if Scoreboard.game_on:
                listen_to_keys()
            else:
                game_over = True
                score.reset_high_score()
                score.thanks_for_playing()

    # Detect collision with tail
    for segment in snake.snake_block_list[2:]:
        if snake.head_of_snake.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
            score.continue_playing()
            if Scoreboard.game_on:
                listen_to_keys()
            else:
                game_over = True
                score.reset_high_score()
                score.thanks_for_playing()



##### Get screen to stay on #####
screen.exitonclick()