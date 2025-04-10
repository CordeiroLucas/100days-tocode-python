class QuizBrain:

	def __init__(self, q_list):
		self.question_number = 0
		self.question_list = q_list
		self.score = 0

	def still_has_questions(self):
		return len(self.question_list) > self.question_number

	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False): ")
		self.check_answer(user_answer, current_question.answer)
	
	def check_answer(self, user_answer, correct_answer):
		if correct_answer.lower() == user_answer.lower():
			print("Right Answer")
			self.score += 1
		else:
			print("Wrong Answer")
		print(f"Correct Answer: {correct_answer}.")
		print(f"Current Score: {self.score}/{self.question_number}")
		print('\n')