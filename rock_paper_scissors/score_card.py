
class ScoreCard:

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def score_card(self, compare):     # Here, we need to pass in the object from ComparePlayers class
        if compare.win:
            self.wins += 1

        elif compare.lose:
            self.losses += 1
        
        elif compare.draw:
            self.draws += 1