import random

def ask_question(question_data):
    """Function to ask a question and check the answer."""
    question = question_data['question']
    correct_answers = question_data['answers']
    points = question_data['points']

    answer = input(question + " ").strip().lower()
    if answer in correct_answers:
        print("Correct Answer! :-)")
        return points
    else:
        print("Incorrect Answer :-(")
        return 0

# Welcome message
print("Welcome to the Quiz!!!!!")
ans = input("Do you want to play? (yes/no) ").strip().lower()

# Quit if the user doesn't want to play
if ans != "yes":
    quit()

# Initialization of the score
user_score = 0
name = input("Enter your name: ").strip()
print(f"Welcome {name}!!!")

# List of questions organized by difficulty
questions = [
    {'question': "What is the capital of M.P.?", 'answers': ["bhopal"], 'points': 10, 'difficulty': 'easy'},
    {'question': "Who is the writer of the famous Harry Potter series?", 'answers': ["j.k. rowling", "jk rowling", "rowling", "j k rowling"], 'points': 10, 'difficulty': 'easy'},
    {'question': "Which actor is also known as Big B?", 'answers': ["amitabh bachchan", "amitabh", "bachchan", "amit ji"], 'points': 10, 'difficulty': 'easy'},
    {'question': "Who is the Prime Minister of India?", 'answers': ["narendra modi", "modi", "modiji", "narendra damodardas modi"], 'points': 10, 'difficulty': 'easy'},
    {'question': "Which coding language is known as the backbone of web development?", 'answers': ["javascript"], 'points': 20, 'difficulty': 'medium'},
    {'question': "What is the chemical symbol for gold?", 'answers': ["au"], 'points': 20, 'difficulty': 'medium'},
    {'question': "Who developed the theory of relativity?", 'answers': ["albert einstein", "einstein"], 'points': 20, 'difficulty': 'medium'},
    {'question': "What is the capital of Australia?", 'answers': ["canberra"], 'points': 20, 'difficulty': 'medium'},
    {'question': "What is the square root of 256?", 'answers': ["16"], 'points': 30, 'difficulty': 'hard'},
    {'question': "Who painted the Mona Lisa?", 'answers': ["leonardo da vinci", "da vinci"], 'points': 30, 'difficulty': 'hard'},
    {'question': "What is the powerhouse of the cell?", 'answers': ["mitochondria"], 'points': 30, 'difficulty': 'hard'},
    {'question': "What is the capital of Iceland?", 'answers': ["reykjavik"], 'points': 30, 'difficulty': 'hard'},
]

# Shuffle questions to randomize the order
random.shuffle(questions)

# Initialize current difficulty level
current_difficulty = 'easy'

# Function to get the next question based on current difficulty
def get_next_question():
    for q in questions:
        if q['difficulty'] == current_difficulty:
            questions.remove(q)
            return q
    return None

# Game loop
while True:
    question_data = get_next_question()
    if not question_data:
        print("Congratulations! You've answered all questions correctly!")
        break

    points = ask_question(question_data)
    if points == 0:
        print(f"Game Over! Your final score is: {user_score}")
        break
    else:
        user_score += points
        print(f"Your current score is: {user_score}")

    # Increase difficulty after certain points
    if user_score >= 40 and current_difficulty == 'easy':
        current_difficulty = 'medium'
        print("Advancing to Medium difficulty questions!")
    elif user_score >= 100 and current_difficulty == 'medium':
        current_difficulty = 'hard'
        print("Advancing to Hard difficulty questions!")
