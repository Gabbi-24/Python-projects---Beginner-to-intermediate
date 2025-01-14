import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps_dict = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors,
}



game_art = r"""
   __            _         __                                   __           _                        
  /__\ ___   ___| | __    / /  _ __   __ _ _ __   ___ _ __     / /  ___  ___(_)___ ___  ___  _ __ ___ 
 / \/// _ \ / __| |/ /   / /  | '_ \ / _` | '_ \ / _ \ '__|   / /  / __|/ __| / __/ __|/ _ \| '__/ __|
/ _  \ (_) | (__|   <   / /   | |_) | (_| | |_) |  __/ |     / /   \__ \ (__| \__ \__ \ (_) | |  \__ \
\/ \_/\___/ \___|_|\_\ /_/    | .__/ \__,_| .__/ \___|_|    /_/    |___/\___|_|___/___/\___/|_|  |___/
                              |_|         |_|                                                         
"""