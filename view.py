from tkinter import *

FONT = ("Arial", 20, "italic")
BACKGROUND_COLOR = '#316B83'


class View:
    def __init__(self, controller):
        self.quiz_panel = self.Quiz_panel(controller)
        self.choice_buttons = self.Buttons(controller)

    class Quiz_panel:
        def __init__(self, controller):
            self.score_label = Label(text="Score: 0", fg='white', bg=BACKGROUND_COLOR, font=FONT)
            self.score_label.grid(row=0, column=1)
            self.info_label = Label(text=f"category: X  Difficulty: X", fg='white', bg=BACKGROUND_COLOR, font=FONT)
            self.info_label.grid(row=1, column=0, columnspan=2)
            self.canvas = Canvas(width=300, height=250, bg='white')
            self.question = self.canvas.create_text(
                150,
                125,
                width=280,
                text='Some Text',
                font=FONT,
                fill=BACKGROUND_COLOR
            )
            self.canvas.grid(row=2, column=0, columnspan=2, pady=40)

    class Buttons:
        def __init__(self, controller):
            self.true_img = PhotoImage(file='image/true.png')
            self.false_img = PhotoImage(file='image/false.png')
            self.right_button = Button(image=self.true_img, highlightthickness=0, command=controller.view_right_button_press)
            self.wrong_button = Button(image=self.false_img, highlightthickness=0, command=controller.view_wrong_button_press)
            self.right_button.grid(row=3, column=0, )
            self.wrong_button.grid(row=3, column=1)


# class Menu:
#     def __init__(self, controller):
#         labels
        # self.title_label = Label(text=f"Choose the game options", fg='white', bg=BACKGROUND_COLOR, font=FONT)
        # self.amount_label = Label(text=f"Number of Questions:", fg='white', bg=BACKGROUND_COLOR, font=FONT)
        # self.category_label = Label(text=f"Select Category:", fg='white', bg=BACKGROUND_COLOR, font=FONT)
        # self.difficulty_label = Label(text=f"Select Difficulty:", fg='white', bg=BACKGROUND_COLOR, font=FONT)
        # self.title_label.grid(row=0, column=0, columnspan=2)
        # self.amount_label.grid(row=1, column=0, columnspan=2)
        # self.category_label.grid(row=3, column=0, columnspan=2)
        # self.difficulty_label.grid(row=5, column=0, columnspan=2)
        #
        #
        # spinboxes
        # self.question_amount_spinbox = Spinbox(from_=5, to=50,)
        # self.question_category_spinbox = Spinbox(values=controller.model.categories)
        # self.question_difficulty_spinbox = Spinbox(values=controller.model.difficulty)
        # self.question_amount_spinbox.grid(row=2, column=0, columnspan=2)
        # self.question_category_spinbox.grid(row=4, column=0, columnspan=2)
        # self.question_category_spinbox.grid(row=6, column=0, columnspan=2)

