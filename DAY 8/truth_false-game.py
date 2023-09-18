# True/False Quiz Game

# Define a list of questions and their corresponding answers (True or False).
questions = [
    {"question": "Python is a programming language.", "answer": True},
    {"question": "The sun is the largest planet in our solar system.", "answer": False},
    {"question": "Water boils at 373 degrees kelvin at sea level.", "answer": True},
    {"question": "The capital of Bnagladesh is Nowakhali.", "answer": False},
    {"question": "The Earth is flat.", "answer": False}
]

# Initialize the player's score.
score = 0

# Function to ask a True/False question and check the answer.
def ask_question(question_obj):
    global score
    print(question_obj["question"])
    user_answer = input("True or False? ").strip().lower()
    
    if user_answer == "true" or user_answer == "t":
        user_answer = True
    elif user_answer == "false" or user_answer == "f":
        user_answer = False
    else:
        print("Invalid input. Please enter 'True' or 'False'.")
        return
    
    if user_answer == question_obj["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

# Loop through the questions and ask them one by one.
for q in questions:
    ask_question(q)

# Display the final score.
print(f"Your score: {score}/{len(questions)}")
