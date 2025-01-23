from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from player_name import PlayerName
import time

##### Create screen #####
screen = Screen()
screen.setup(width=1526, height=800, startx=0, starty=0)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


##### Divide the screen for the 2 players #####
divider = Turtle()
divider.pensize(5)
divider.penup()
divider.hideturtle()
divider.color("white")
divider.goto(0, 395)
divider.setheading(270)
for item in range(20):
    divider.pendown()
    divider.forward(20)
    divider.penup()
    divider.forward(20)

screen.update()


##### Create Player paddles #####
player_1 = Paddle()
player_1.create_paddle_player1()
player_2 = Paddle()
player_2.create_paddle_player2()
screen.update()


##### Create player names #####
player_names = PlayerName(screen)


##### Create ball #####
pong_ball = Ball(player_names.difficulty)


##### Create score #####
player1_score = ScoreBoard(-60)
player2_score = ScoreBoard(60)



##### Listen for input and assign keys #####
screen.listen()
# Up movement control
screen.onkeypress(fun=player_1.move_paddle_up, key="w")
screen.onkeyrelease(fun=player_1.stop_paddle_up, key="w")
screen.onkeypress(fun=player_2.move_paddle_up, key="Up")
screen.onkeyrelease(fun=player_2.stop_paddle_up, key="Up")

# Down movement control
screen.onkeypress(fun=player_1.move_paddle_down, key="s")
screen.onkeyrelease(fun=player_1.stop_paddle_down, key="s")
screen.onkeypress(fun=player_2.move_paddle_down, key="Down")
screen.onkeyrelease(fun=player_2.stop_paddle_down, key="Down")


##### MAIN CODE #####
player_names.write_player_name(-380, player_names.player1_name)
player_names.write_player_name(380, player_names.player2_name)

end_game = False

while not end_game:
    # if player_names.difficulty == "1":
    #     time.sleep(0.08)
    # elif player_names.difficulty == "2":
    #     time.sleep(0.05)
    # elif player_names.difficulty == "3":
    #     time.sleep(0.02)
    time.sleep(pong_ball.move_speed)
    pong_ball.move_ball()
    player_1.move()
    player_2.move()
    screen.update()
    # pong_ball.random_heading_left(player_1, player_2)
    # screen.update()
    if pong_ball.ycor() < -385 or pong_ball.ycor() > 385:   # Ball collides with top or bottom
        pong_ball.setheading(-pong_ball.heading())
    if pong_ball.xcor() < -752:     # Player 1 loses
        end_game = True
        if player1_score.score == player2_score.score:
            player1_score.game_over("Nobody")
        else:
            player1_score.game_over(player_names.player2_name)
    elif pong_ball.xcor() > 752:    # Player 2 loses
        end_game = True
        if player1_score.score == player2_score.score:
            player1_score.game_over("Nobody")
        else:
            player1_score.game_over(player_names.player1_name)
    elif any(pong_ball.distance(block) < 27 for block in player_1.paddle):    # Ball collides with player 1 paddle
        pong_ball.random_heading_right(player_1)
        player1_score.update_score()
        pong_ball.move_speed *= 0.9   # Increase the speed a little as game progresses
    elif any(pong_ball.distance(block) < 27 for block in player_2.paddle):    # Ball collides with player 2 paddle
        pong_ball.random_heading_left(player_2)
        player2_score.update_score()   # Increase the speed a little as game progresses
        pong_ball.move_speed *= 0.9




##### Make sure screen stays on #####
screen.exitonclick()