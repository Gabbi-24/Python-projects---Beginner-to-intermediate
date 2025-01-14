# TODO 3: Create a class to ask user a question, check answer and see if the quiz is finished

class QuizBrain:

    def __init__(self, question_list):    # Basically we want to input the question_bank here when creating object
        self.question_number = 0          # To keep track of what question we are on
        self.question_list = question_list
        self.score = 0                    # To keep track of user's score


    def next_question(self):
        current_question = self.question_list[self.question_number]  # To keep track of the current question content
        self.question_number += 1

        while True:
            # Now call the attribute of text from the object (since it was created under Question class
            user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)?: ").title()
            if user_answer in ["True", "False"]:
                break
            else:
                print("Invalid input. Please type either 'True' or 'False'.\n")

        self.__check_answer(current_question, user_answer)

    def still_has_questions(self):
        question_left = len(self.question_list) - self.question_number

        # if question_left > 0:   # An inequality already get evaluated as a boolean so you can simplify like I did below
        #     return True
        # else:
        #     return False

        return question_left > 0

    # Call this next method inside next_question() method
    #-- This allows us to feed in local variables from the next_question() method into the check_answer() method
    def __check_answer(self, question_in_progress, answer):   # Making this method private
        if answer == question_in_progress.answer:
            self.score += 1
            print("You're right! 😎")

        else:
            print("Oops, that's wrong. 🤪")

        print(f"The correct answer is: {question_in_progress.answer}.\n"
              f"Your current score is: {self.score}/{self.question_number}.\n")






