from tkinter import *
from model import Model
from view import View, Menu

BACKGROUND_COLOR = '#316B83'


class Controller:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.root.title("Quiz")
        self.root.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
        self.view = Menu(self)
        self.timer: object
        self.root.mainloop()

    # ---------- Model related methods ----------

    def model_generate_api_parameters(self):
        # Sets the API parameters
        amount = self.view.question_amount_spinbox.get()
        category = self.view.question_category_spinbox.get()
        difficulty = self.view.question_difficulty_spinbox.get()
        if difficulty != 'Any':
            self.model.parameters['difficulty'] = difficulty.lower()
        if category != "Any Category":
            self.model.parameters['category'] = self.model.categories_api[category]['value']
        self.model.parameters['amount'] = amount
        self.view.next_button.config(state=NORMAL)


    def model_set_parameters(self):
        self.model.bank = self.model.build_question_bank()
        print("BANK TEST", self.model.bank)
        # delete all the widgets for the screen change
        self.view.question_amount_spinbox.grid_forget()
        self.view.question_category_spinbox.grid_forget()
        self.view.question_difficulty_spinbox.grid_forget()
        self.view.title_label.grid_forget()
        self.view.amount_label.grid_forget()
        self.view.category_label.grid_forget()
        self.view.difficulty_label.grid_forget()
        self.view.generate_button.grid_forget()
        self.view.next_button.grid_forget()
        # sets new screen
        self.view = View(self)
        self.timer = self.root.after(1, func=self.view_next_question)
        self.view_next_question()

    # ---------- View related methods ----------

    def set_view(self):
        pass

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
        # if there's no more question in the bank it's game over
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

        else:
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
        gues_srate = (self.model.score * 100) / int(self.model.parameters['amount'])
        msg = f"Results:\n" \
              f"final score:{self.model.score}/{self.model.parameters['amount']}\n" \
              f"You got {gues_srate}% of the questions\n" \
              f"Thank you for playing\n" \

        if gues_srate < 100:
            self.view.quiz_panel.canvas.itemconfig(self.view.quiz_panel.question, text=msg)
        else:
            self.view.quiz_panel.canvas.itemconfig(self.view.quiz_panel.question,
                                                   text="You hit on teh spot!!!\n"
                                                        "You got 100%\n"
                                                        "Congratulations")

        self.view.choice_buttons.right_button.config(state=DISABLED)
        self.view.choice_buttons.wrong_button.config(state=DISABLED)


