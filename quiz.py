def ask_question(question, correct_answers):
    """Function to ask a question and check the answer."""
    answer = input(question).lower()
    if answer in correct_answers:
        print("Correct Answer :-) ")
        return 1
    else:
        print("Incorrect Answer :-(")
        return 0

# Welcome message
print("Welcome to the Quiz!!!!!")
ans = input("Do you want to play? ").lower()

# Quit if the user doesn't want to play
if ans != "yes":
    quit()

# Initializing the score
userscore = 0
name = input("Enter your name: ")
print(f"Welcome {name}!!!")

# Question 1
userscore += ask_question("What is the capital of M.P.? ", ["bhopal"])

# Question 2
userscore += ask_question("Who is the writer of the famous Harry Potter series? ", 
                          ["j.k.rowling", "jk rowling", "rowling", "j k rowling"])

# Question 3
userscore += ask_question("Which actor is also known as Big B? ", 
                          ["amitabh bachchan", "amitabh", "bachchan", "amit ji"])

# Question 4
userscore += ask_question("Who is the Prime Minister of India? ", 
                          ["narendra modi", "modi", "modiji", "narendra damodardas modi"])

# Question 5
userscore += ask_question("Which coding language is the best? ", ["python"])

# Final score
print(f"\n{name}'s Total Score is: {userscore}")
print("Thank You for Playing!!!!!")
print(f"${'$'*15}")
