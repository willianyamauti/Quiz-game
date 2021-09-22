from tkinter import *
from model import Model
from view import View
import random
import html

BACKGROUND_COLOR = '#316B83'


class Controller:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = View(self)
        self.root.title("Quiz")
        self.root.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
        self.timer = self.root.after(1, func=self.view_next_question)
        self.view_update_score()
        self.root.mainloop()

    # ---------- Model related methods ----------

    def model_set_question_number(self):
        self.model.parameters['amount'] = self.view.question_amount_spinbox.get()

    # ---------- View related methods ----------
    def view_next_question(self):
        try:
            self.root.after_cancel(self.timer)
            self.model.fetch_new_question()
            question = self.model.question.text
            self.view.quiz_panel.canvas.itemconfig(self.view.quiz_panel.question, text=question)
            self.view.quiz_panel.info_label.config(text=f"{self.model.question.category}")
            #                                             f"Difficulty: {self.model.question.difficulty}")

            self.view.choice_buttons.right_button.config(state=NORMAL)
            self.view.choice_buttons.wrong_button.config(state=NORMAL)

        except ValueError as err:
            self.view_game_over()

    def view_update_score(self):
        self.view.quiz_panel.score_label.config(text=f"Score {self.model.score} / {self.model.parameters['amount']}")

    def view_check_answer(self, answer: str):
        if self.model.question.answer == answer:
            self.model.score += 1
            self.view_update_score()
            # displays if the player get the question right for 2 sec
            self.timer = self.root.after(1000, func=self.view_next_question)
            self.view.quiz_panel.canvas.itemconfig(self.view.quiz_panel.question, text=f"CORRECT!!!")
            self.view.choice_buttons.right_button.config(state=DISABLED)
            self.view.choice_buttons.wrong_button.config(state=DISABLED)
            # self.view.quiz_panel.info_label.config(text=f"CORRECT!!!")
        else:
            # self.view.quiz_panel.info_label.config(text=f"Incorrect!!!")
            self.view.quiz_panel.canvas.itemconfig(self.view.quiz_panel.question, text=f"INCORRECT!!!")
            self.view.choice_buttons.right_button.config(state=DISABLED)
            self.view.choice_buttons.wrong_button.config(state=DISABLED)
            self.timer = self.root.after(1200, func=self.view_next_question)

    def view_right_button_press(self):
        self.view_check_answer('True')

    def view_wrong_button_press(self):
        self.view_check_answer('False')

    def view_game_over(self):
        self.view.quiz_panel.score_label.config(text=f"GAME OVER")
        self.view.quiz_panel.info_label.config(text=f"You guessed all questions!")
        guessrate = (self.model.score * 100) / self.model.parameters['amount']
        msg = f"Results:\n" \
              f"final score:{self.model.score}/{self.model.parameters['amount']}\n" \
              f"You got {guessrate}% of the questions\n" \
              f"Thank you for playing\n" \

        if guessrate < 100:
            self.view.quiz_panel.canvas.itemconfig(self.view.quiz_panel.question, text=msg)
        else:
            self.view.quiz_panel.canvas.itemconfig(self.view.quiz_panel.question,
                                                   text="You hit on teh spot!!!\n"
                                                        "You got 100%\n"
                                                        "Congratulations")

        self.view.choice_buttons.right_button.config(state=DISABLED)
        self.view.choice_buttons.wrong_button.config(state=DISABLED)


