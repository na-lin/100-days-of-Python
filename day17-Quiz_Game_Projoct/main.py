from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# TODO 2: write a for loop to iterate over the question_data
# TODO 2: create a Question object from each entry in question_data
# TODO 2: append each Question object to the question_bank.

# My solution : name is not clear like teacher's solution
# question_bank = []
# for data in question_data:
#     question = Question(data["text"], data["answer"])
#     question_bank.append(question)
# print(question_bank)

# Teacher's solution and name style
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)

# My solution of
# quiz_game = QuizBrain(question_bank)
# next_question_number = quiz_game.question_number
# next_question = question_bank[next_question_number].text
# quiz_game.next_question(next_question_number,next_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():

    quiz.next_question()
# TODO 7: print out result
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score} / {quiz.question_number}.")