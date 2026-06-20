from quiz_brain import QuizBrain
from data import question_data
startQuiz=QuizBrain()
startQuiz.add_question(question_data)
startQuiz.call_next_question()
