
class ComparePlayers:

    def __init__(self, computer, user):
        self.computer = computer
        self.user = user
        self.win = None
        self.lose = None
        self.draw = None
    
    
    def compare(self):
        # Reset outcomes at the start of each comparison
        #-- Because I want to store it globally for object but the outcome needs to be reset for each round
        self.win = None
        self.lose = None
        self.draw = None

        if self.user == self.computer:
            self.draw = True
            print(f"\n***** It's a draw! *****\n")

        elif self.user == "rock":
            if self.computer == "scissors":
                self.win = True
                print(f"\n***** You win! *****\n")
            elif self.computer == "paper":
                self.lose = True
                print(f"\n***** You lose! *****\n")

        elif self.user == "paper":
            if self.computer == "rock":
                self.win = True
                print(f"\n***** You win! *****\n")
            elif self.computer == "scissors":
                self.lose = True
                print(f"\n***** You lose! *****\n")

        elif self.user == "scissors":
            if self.computer == "paper":
                self.win = True
                print(f"\n***** You win! *****\n")
            elif self.computer == "rock":
                self.lose = True
                print(f"\n***** You lose! *****\n")


    
