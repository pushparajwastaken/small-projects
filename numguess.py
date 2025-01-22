import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    compguess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            userguess = int(input(f"Enter a number between 1 and 100 (Attempts left: {attempts}): "))
            if userguess < 1 or userguess > 100:
                print("Please enter a number within the range 1 to 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if compguess == userguess:
            print("Congratulations! You guessed the correct number!")
            break
        elif userguess < compguess:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")

        attempts -= 1

    if attempts == 0:
        print(f"Game Over! The correct number was {compguess}.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing! Goodbye!")
        break
