# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz


# TODO 3: create a class called QuizBrain
# TODO 3: write an __init__ method ,to initialize the question_number to 0
# TODO 3: initialize the question_list to an input

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # TODO 4: retrieve the item at the current question_number from the question_list
    # TODO 4: use the input() function to show the user the Question text and ask for the user's answer
    # MY solution
    # def next_question(self, q_number, q_list):
    #
    #     input(f"Q.{q_number + 1 }: {q_list} (True or False)?: ")

    # TODO 5: Still has questiosn
    def still_has_question(self):
        number_of_question = len(self.question_list)
        if self.question_number > number_of_question - 1:
            return False
        return True
        # return self.question_number < number_of_question

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_text = current_question.text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_text}(True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    # TODO 6: check correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
