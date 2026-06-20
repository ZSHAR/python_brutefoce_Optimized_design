from question_model import Question
from data import question_data

class QuizBrain:
    score=0
    def __init__(self):
        self.question_number=0
        self.question_list=0
        self.question_bank=[]

    def add_question(self,question_data):
        for question in question_data:
            question_text = question["text"]
            question_answer = question["answer"]
            new_question = Question(question_text, question_answer)
            self.question_bank.append(new_question)

    def next_question(self):
        capture_answer=input(f"Q:{self.question_number+1} {self.question_bank[self.question_number].question} true or false").lower()
        if capture_answer == self.question_bank[self.question_number].answer.lower():
            self.score+=1
            print("you answered correctly")
        else:
            print("you answered incorrectly")
        print(f"your score is {self.score}/{self.question_number+1}")
        self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.question_bank)

    def call_next_question(self):
        while self.still_has_question():
            self.next_question()

