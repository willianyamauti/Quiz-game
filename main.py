from data import question_data
from question_model import Question
from quiz_brain import Quizz
from random import randint

question_bank = [Question(*text.values()) for text in question_data]
quiz = Quizz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed the quiz!\n"
      f"Your final Score is {quiz.score}/{quiz.question_number}")