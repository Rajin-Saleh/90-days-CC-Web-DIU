import random

class QuizQuestion:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def generate_quiz(self, num_questions=5):
        random.shuffle(self.questions)
        return self.questions[:num_questions]

def main():
    quiz = Quiz()

    # Add questions to the quiz
    question1 = QuizQuestion("What is the capital of France?",
                             ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
                             "A")
    question2 = QuizQuestion("Which planet is known as the Red Planet?",
                             ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
                             "B")
    question3 = QuizQuestion("What is the largest mammal in the world?",
                             ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Lion"],
                             "C")

    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)

    num_questions_to_ask = 3
    quiz_questions = quiz.generate_quiz(num_questions_to_ask)

    score = 0
    for i, question in enumerate(quiz_questions, 1):
        print(f"Question {i}: {question.question}")
        for choice in question.choices:
            print(choice)
        user_answer = input("Your answer (e.g., 'A', 'B', 'C', 'D'): ").upper()
        if question.is_correct(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question.correct_answer}.\n")

    print(f"You got {score} out of {num_questions_to_ask} questions correct.")

if __name__ == "__main__":
    main()

