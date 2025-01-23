import time
import random
from idlelib.editor import keynames
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#### Screen setup #####
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

##### Create Player Object #####
player = Player()

##### Listen for input and move player up and down with keys #####
screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")          # NB!!!: Do not put method brackets or the method is called immediately
screen.onkeyrelease(fun=player.stop_moving, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")
screen.onkeyrelease(fun=player.stop_moving, key="Down")


##### Create scoreboard object #####
score = Scoreboard()


##### Create function for cars #####
car_list = []

def create_cars():
    if score.level_number == 1:
        random_list = ["", "", "", "", "", "", "", CarManager(player)]
    elif score.level_number == 2:
        random_list = ["", "", "", "", "", CarManager(player)]
    elif score.level_number == 3:
        random_list = ["", "", "", CarManager(player)]
    elif score.level_number == 4:
        random_list = ["", CarManager(player)]
    else:
        random_list = [CarManager(player)]
    car_list.append(random.choice(random_list))
    for item in car_list:
        if item != "":
            item.move_car()


##### Game loop #####
game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    player.check_player_position()
    score.level_text()
    create_cars()
    if Player.restarted:
        CarManager(player).increase_speed()
    if CarManager.collision:
        score.game_ends()
        game_over = True



##### Keep Screen On #####
screen.exitonclick()