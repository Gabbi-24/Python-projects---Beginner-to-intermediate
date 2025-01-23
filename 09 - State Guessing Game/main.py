import turtle
from turtle import Turtle
from end_game import EndGame

import pandas

from organising_states import States

##### Create screen #####
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


##### Get csv data #####
data_csv = pandas.read_csv("50_states.csv")


##### Create States object #####
states = States(data_csv)
state_list = states.get_state_list()


##### Object for end of game writing #####
end_game_writing = EndGame()


##### Game loop #####
game_over = False
correct_answers = 0
list_correct_guesses = []

while not game_over:
    player_answer = screen.textinput(f"{correct_answers}/50 States Correct", "Guess the name of a US state:")

    if player_answer is None:
        end_game_writing.lose_game_writing(correct_answers)
        learn_states_df = pandas.DataFrame(state_list)
        learn_states_df.to_csv("states_to_learn.csv")
        game_over = True

    else:
        player_answer = player_answer.title()

        if player_answer in state_list:
            states.write_state(player_answer)
            state_list.remove(player_answer)
            correct_answers += 1
            list_correct_guesses.append(player_answer)

            if correct_answers == 50:
                end_game_writing.win_game_writing()
                game_over = True

        elif player_answer == "Exit":
            end_game_writing.lose_game_writing(correct_answers)
            learn_states_df = pandas.DataFrame(state_list)
            learn_states_df.to_csv("states_to_learn.csv")
            game_over = True







##### Keep screen on #####
screen.exitonclick()