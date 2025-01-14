from turtle import Turtle, Screen

FONT_SIZE = 40

class PlayerName(Turtle):    # Can't inherit from both Screen and Turtle

    def __init__(self, screen_object: Screen):   # Tells Python and coders to expect this input to be an instance of Screen class
        super().__init__()
        self.screen = screen_object
        self.hideturtle()
        self.penup()
        self.color("white")
        self.player1_name = None
        self.player2_name = None
        self.difficulty = None
        self.get_player_name()
        self.get_difficulty()


    def get_player_name(self):
        self.player1_name = self.screen.textinput("Player 1", "Name of Player 1:")
        self.player2_name = self.screen.textinput("Player 2", "Name of Player 2:")


    def get_difficulty(self):
        self.difficulty = self.screen.textinput("Difficulty level", f"Choose your difficulty level (type only the number):\n"
                                     f"1) Easy\n"
                                     f"2) Normal\n"
                                     f"3) Difficult")


    def write_player_name(self, x_cor, player):
        self.setposition(x_cor, 340)
        self.write(f"{player}", align="center", font=("Haettenschweiler", FONT_SIZE, "normal"))