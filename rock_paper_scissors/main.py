from define_players import DefinePlayers
from round_num import Rounds
from art import game_art
from compare_players import ComparePlayers
from score_card import ScoreCard
import os

# Clear console func
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



# Main code
clear_console()
print(game_art)
#-- Create object that must only be created once and, therefore, mustn't be part of the loop
num_of_rounds = Rounds() # Create object for Rounds
computer_player = DefinePlayers()   # Create the computer player
user_player = DefinePlayers()    # Create the user player
score = ScoreCard()    # Create a score card

while num_of_rounds.rounds_left > 0:
    clear_console()
    print(game_art)
    print(f"Round {num_of_rounds.current_round}/{num_of_rounds.round_total}... Let's Play!\n")

    compare_players = ComparePlayers(computer = computer_player.computer_setup(),
                                     user = user_player.user_setup())
    
    computer_player.print_computer_choice()
    user_player.print_user_choice()

    compare_players.compare()

    score.score_card(compare_players)

    print(f"Here is your scorecard:\n"
          f"Wins: {score.wins}\n"
          f"Losses: {score.losses}\n"
          f"Draws: {score.draws}\n")
    
    num_of_rounds.calc_rounds()

    input(f"\nHit enter to continue...")
        

clear_console()
print(game_art)
print(f"Thank you for playing!\n")
print(f"Until next time...\n")

