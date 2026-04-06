


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.current_score = 0
        self.final_score = 0
        # self.answers_list = True

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}:{current_question.text} (True/False):").lower()
        self.check_answer(user_answer, current_question.answer)
        print("\n"*1)

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            print(f"The correct answer is {correct_answer}.")
            self.current_score += 1
            print(f"Your current score is: {self.current_score}/{self.question_number + 1}")
            return True
        else:
            print(f"You got it wrong. The correct answer is {correct_answer}.")
            print(f"Your current score is: {self.current_score}/{self.question_number + 1}")
            return False


    def still_has_questions(self):

        self.question_number += 1

        return True if self.question_number < len(self.questions_list) else False



