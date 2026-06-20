from question_model import Question
from data import question_data
question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
score=0
count=0
for question in question_bank:
    answer=input(f"{question.question}True or False: ").lower()
    count+=1
    if answer==question.answer.lower():
        print("Your answer is correct!")
        score+=1
    else:
        print("Your answer is incorrect!")
    print(f"Your score is {score}/{count}")