
class Rounds:

    def __init__(self):
        while True:
            try:
                self.rounds_left = int(input("How many rounds would you like to play?: "))
                break

            except ValueError:
                print(f"\nInvalid input. Please type a numeric number.\n")

        self.current_round = 1

        self.round_total = self.rounds_left


    def calc_rounds(self):
         self.rounds_left -= 1
         self.current_round += 1
        