from turtle import Turtle, Screen

FONT_SCORE = ("Arial", 16, "normal")
FONT_GAME_OVER = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    screen_temp = Screen()
    game_on = True

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = None
        self.retrieve_high_score()


    def display_score(self):
        self.goto(0, 270)
        self.clear()
        score_heading = f"Your current score: {self.score}"
        high_score_heading = f"Your high score: {self.high_score}"
        self.write(f"{score_heading}     {high_score_heading}", move=False, align="center", font=FONT_SCORE)


    def update_score(self):
        self.score += 1

    def thanks_for_playing(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.color("maroon1")
        thanks_text = (f"Thank you for playing!\n"
                       f"Your high score is: {self.high_score}")
        self.write(thanks_text, move=False, align="center", font=FONT_GAME_OVER)

    # No longer want to end the game but rather restart it and update te highscore if necessary
    # def game_over(self):
    #     self.clear()
    #     self.penup()
    #     self.goto(0,0)
    #     self.color("maroon1")
    #     game_over_text = f"Game Over! Your final score is: {self.score}"
    #     self.write(game_over_text, move=False, align="center", font=FONT_GAME_OVER)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.store_high_score()
        self.score = 0
        self.display_score()

    def store_high_score(self):
        try:
            stream = open("high_score.txt", "w")
            stream.write(f"{self.high_score}")
            stream.close()

        except Exception as e:
            print(e)

    def retrieve_high_score(self):
        try:
            stream = open("high_score.txt", "r")
            self.high_score = int(stream.read())
            stream.close()

        except OSError:
            self.high_score = 0

        except Exception as e:
            print(e)

    def continue_playing(self):
        while True:
            try:
                player_input = Scoreboard.screen_temp.textinput(f"Do you want to keep playing?",
                                                      f"Please type only the number corresponding to your choice:\n"
                                                      f"1. Yes\n"
                                                      f"2. No")
                player_input = int(player_input)
                if player_input == 1:
                    break
                elif player_input == 2:
                    Scoreboard.game_on = False
                    break
                else:
                    print("Please input a valid number.")

            except ValueError:
                print("Please input only the number corresponding to your chosen option.")


    def reset_high_score(self):
        while True:
            try:
                player_input = Scoreboard.screen_temp.textinput(f"Reset high score to 0 for future games?",
                                                            f"Please type only the number corresponding to your choice:\n"
                                                                   f"1. Yes, reset the high score to zero.\n"
                                                                   f"2. No, I want to know what to beat next time.")

                player_input = int(player_input)
                if player_input == 1:
                    try:
                        stream = open("high_score.txt", "w")
                        stream.write(f"0")
                        stream.close()

                    except Exception as e:
                        print(e)
                    break

                elif player_input == 2:
                    break
                else:
                    print("Please input a valid number.")

            except ValueError:
                print("Please input only the number corresponding to your chosen option.")


