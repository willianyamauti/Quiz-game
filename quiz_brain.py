from data import question_data


class Quizz:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        qt = self.question_list[self.question_number]
        self.question_number += 1
        aw = input(f'Q.{self.question_number}: {qt.question} (Turue/False)?: ')

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {question_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n ")
