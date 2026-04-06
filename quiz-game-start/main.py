import question_model
import data
from quiz_brain import QuizBrain


question_bank = []

for key in data.question_data:
    question = question_model.Question(key["question"], key["correct_answer"])
    question_bank.append(question)

QuizBrain = QuizBrain(question_bank)
QuizBrain.next_question()
Final_score = 0

while QuizBrain.still_has_questions():
    QuizBrain.next_question()

Final_score = QuizBrain.current_score
print(f"You've completed the quiz\nYour final score was: {Final_score}/{len(question_bank)}")


