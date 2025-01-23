from turtle import Turtle
FONT = ("Arial", 8, "normal")

class States:
    def __init__(self, csv_input):
        self.data = csv_input
        self.state_list = []

    def get_state_list(self):
        self.state_list = self.data.state.to_list()
        return self.state_list

    def write_state(self, correct_input):     # If a player's guess is correct, it get's inputted here
        correct_guess_row = self.data[self.data.state == correct_input]
        correct_guess_xcoord = correct_guess_row.x.item()    # Accesses the item in the series that we want
        correct_guess_ycoord = correct_guess_row.y.item()

        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(correct_guess_xcoord, correct_guess_ycoord)
        turtle.write(f"{correct_input}", align="center", font=FONT)