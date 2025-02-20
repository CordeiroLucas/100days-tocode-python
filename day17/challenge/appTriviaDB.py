from question_model import Question
from triviaDB import *
from quiz_brain import QuizBrain

# ========================================

import requests

q_difficulty = "difficulty=" + input("Choose the Quiz Difficulty (Easy, Medium, Hard): ").lower()

quiz_response = requests.get(API_URL + QUIZ_AMOUNT + '&' + q_difficulty + '&type=boolean')

if quiz_response.json()['response_code'] == 0:
    quiz_data = quiz_response.json()['results']

# ========================================

question_bank = []
for question in quiz_data:
	question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()

print("You Finished The QUIZ!")
print(f"You're Current Score Was: {quiz.score}/{quiz.question_number}")