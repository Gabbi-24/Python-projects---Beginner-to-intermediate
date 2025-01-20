from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import additional_trivia_questions

# TODO 2: Create a list of Question Objects from Data

question_bank_1 = []
for item in question_data:
    question_bank_1.append(Question(item["text"], item["answer"]))

question_bank_2 = []
for item in additional_trivia_questions.additional_question_data_1:
    question_bank_2.append(Question(item["question"], item["correct_answer"]))


# TODO 4: Create a QuizBrain object

quiz = QuizBrain(question_bank_1)

quiz_2 = QuizBrain(question_bank_2)


# TODO 5: Create a while loop for quiz

# Main code
while quiz.still_has_questions():
    quiz.next_question()

if quiz.score >= 9:
    print(f"Your final score is {quiz.score}/{quiz.question_number}.\n"
          f"Well done! 🤩\n\n"
          f"That's it for now...\n")

elif 4 <= quiz.score < 9:
    print(f"Your final score is {quiz.score}/{quiz.question_number}.\n"
          f"Not too bad, lol 😅\n\n"
          f"That's it for now...\n")

else:
    print(f"Your final score is {quiz.score}/{quiz.question_number}.\n"
          f"Oof! That was rough! 😶\n\n"
          f"That's it for now...\n")






# # Quiz 2
# while quiz_2.still_has_questions():
#     quiz_2.next_question()
#
# if quiz_2.score >= 7:
#     print(f"Your final score is {quiz_2.score}/{quiz_2.question_number}.\n"
#           f"Well done! 🤩\n\n"
#           f"That's it for now...\n")
#
# elif 4 <= quiz.score < 7:
#     print(f"Your final score is {quiz_2.score}/{quiz_2.question_number}.\n"
#           f"Not too bad, lol 😅\n\n"
#           f"That's it for now...\n")
#
# else:
#     print(f"Your final score is {quiz_2.score}/{quiz_2.question_number}.\n"
#           f"Oof! That was rough! 😶\n\n"
#           f"That's it for now...\n")
