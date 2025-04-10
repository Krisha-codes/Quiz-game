class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self,u_answer,correct_answer):
        if u_answer.lower()== correct_answer.lower():
            print("You got it write! Keep going.")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is:{self.score}/{self.question_number}")
        print("\n")





