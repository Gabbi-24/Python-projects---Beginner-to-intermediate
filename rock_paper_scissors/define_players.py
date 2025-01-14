from art import rps_dict
import random


class DefinePlayers:

    def __init__(self):
        # Need to create empty attributes so I can both add to them and use them in multiple methods         
        self.computer_choice = None
        self.user_choice = None


    def computer_setup(self):
        self.computer_choice = random.choice(list(rps_dict.keys()))

        return self.computer_choice


    def user_setup(self):
        while True:
            self.user_choice = input("What is your weapon of choice... rock, paper or scissors? ").lower()

            if self.user_choice in ["rock", "paper", "scissors"]:
                break
            else:
                print(f"\nInvalid input. Please type either 'rock', 'paper' or 'scissors'.\n")
     
        return self.user_choice
    

    def print_computer_choice(self):
        choice_art_computer = rps_dict[self.computer_choice]
        print(f"\nThe computer chose: {choice_art_computer}\n")


    def print_user_choice(self):
        choice_art_user = rps_dict[self.user_choice]       
        print(f"You chose: {choice_art_user}\n")


        





