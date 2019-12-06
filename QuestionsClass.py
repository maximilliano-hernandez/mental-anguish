# Max Hernandez, Final Project, CIS 345, !0:30, T Th
import json


class Question:
    def __init__(self, question_number=0, points=0, question_text="", answer_bank=[], answer="", posfeedback="", negfeedback=""):
        self.question_number = 0
        self.points = 0
        self.question_text = ""
        self.answer_bank = []
        self.answer = ""
        self.posfeedback = ""
        self.negfeedback = ""

    def __str__(self):
        return f'Question Number {self.question_number}:\n' \
               f'    Point Value: {self.points}\n' \
               f'    Question Text: {self.question_text}\n' \
               f'    Answer 1: {self.answer_bank[0]}\n' \
               f'    Answer 2: {self.answer_bank[1]}\n' \
               f'    Answer 3: {self.answer_bank[2]}\n' \
               f'    Answer 4: {self.answer_bank[3]}\n' \
               f'    Correct Answer: {self.answer}\n' \
               f'    Positive Feedback: {self.posfeedback}\n' \
               f'    Negative Feedback: {self.negfeedback}\n' \
               f'____________________________________________________________________\n\n'

    @property
    def question_number(self):
        return self.__question_number

    @question_number.setter
    def question_number(self, question_number):
        self.__question_number = question_number

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points

    @property
    def question_text(self):
        return self.__question_text

    @question_text.setter
    def question_text(self, question_text):
        self.__question_text = question_text

    @property
    def answer_bank(self):
        return self.__answer_bank

    @answer_bank.setter
    def answer_bank(self, answer_bank):
        self.__answer_bank = answer_bank

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer):
        self.__answer = answer

    @property
    def posfeedback(self):
        return self.__posfeedback

    @posfeedback.setter
    def posfeedback(self, posfeedback):
        self.__posfeedback = posfeedback

    @property
    def negfeedback(self):
        return self.__negfeedback

    @negfeedback.setter
    def negfeedback(self, negfeedback):
        self.__negfeedback = negfeedback

