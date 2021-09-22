import requests
import random
import html


class Model:
    categories = ["Any Category","General Knowledge", "Entertainment: Books", "Entertainment: Film",
                  "Entertainment: Music", "Entertainment: Musicals &amp; Theatres", "Entertainment: Television",
                  "Entertainment: Video Games", "Entertainment: Board Games", "Science &amp; Nature",
                  "Science: Computers", "Science: Mathematics", "Mythology", "Sports", "Geography", "History",
                  "Politics", "Art", "Celebrities", "Animals", "Vehicles", "Entertainment: Comics", "Science: Gadgets",
                  "Entertainment: Japanese Anime &amp; Manga", "Entertainment: Cartoon &amp; Animations", ]

    difficulty = ['any', 'easy', 'medium', 'hard']

    categories_api = [{'value': value} for value, category in enumerate(categories[1:], 9)]

    parameters = {
        "amount": 10,
        # "category": 'any',
        "type": 'boolean',
        # "difficulty": str,
    }

    def __init__(self):
        self.bank = self.build_question_bank()
        self.score = 0
        self.question = self.Question_model()

    class Question_model:
        def __init__(self):
            self.category = ''
            self.difficulty = ''
            self.text = ''
            self.answer = "boolean"

    def build_question_bank(self):
        # https://opentdb.com/api_config.php
        response = requests.get(url="https://opentdb.com/api.php", params=self.parameters)
        response.raise_for_status()
        data = response.json()
        return data["results"]

    def fetch_new_question(self):
        new_question = self.bank.pop(random.randint(0, len(self.bank) - 1))
        self.question.category = new_question["category"]
        self.question.difficulty = new_question["difficulty"]
        # cleans html entities
        self.question.text = html.unescape(new_question["question"])
        self.question.answer = new_question["correct_answer"]
