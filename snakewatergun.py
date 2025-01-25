import random
import time

def game(user_choice, comp_choice, name):
    """
    Determines the result of a round.
    """
    if user_choice == comp_choice:
        print("It's a Draw!")
        return 0
    elif (user_choice == 1 and comp_choice == 2) or \
         (user_choice == 2 and comp_choice == 3) or \
         (user_choice == 3 and comp_choice == 1):
        print(f"{name} won this round!")
        return 1
    else:
        print("Computer won this round!")
        return -1

def play_game(rounds, name):
    """
    Manages the game flow for a given number of rounds.
    """
    scores = {"user": 0, "computer": 0}
    choices = {1: "Snake", 2: "Water", 3: "Gun"}

    print(f"\n{name}, let's start the game!")
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")

        comp_choice = random.randint(1, 3)

        while True:
            try:
                user_input = int(input("Enter 1 for Snake, 2 for Water, 3 for Gun: "))
                if user_input in choices:
                    break
                else:
                    print("Invalid input! Please choose 1, 2, or 3.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        print(f"Computer chose: {choices[comp_choice]}")
        print(f"{name} chose: {choices[user_input]}")
        
        # Determine round result
        result = game(user_input, comp_choice, name)
        if result == 1:
            scores["user"] += 1
        elif result == -1:
            scores["computer"] += 1

        # Display current scores
        print(f"Scores after round {round_num}: {name}: {scores['user']} | Computer: {scores['computer']}")
        time.sleep(1)

    # Final Results
    print("\nGame Over!")
    display_final_scores(scores, name)

def display_final_scores(scores, name):
    """
    Displays the final scores and announces the winner.
    """
    print(f"\nFinal Scores - {name}: {scores['user']} | Computer: {scores['computer']}")
    if scores["user"] > scores["computer"]:
        print(f"Congratulations {name}, you won the game!")
    elif scores["user"] < scores["computer"]:
        print("Computer won the game! Better luck next time!")
    else:
        print("It's a Draw!")
if __name__ == "__main__":
    print("Welcome to the Snake, Water, and Gun Game!")
    name = input("Enter your name: ")
    while True:
        try:
            rounds = int(input("Enter the number of rounds you want to play: "))
            if rounds > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    play_game(rounds, name)


 
