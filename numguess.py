import random
print("Welcome to the Game of Number Guessing!!!!!")
while True:
    compguess=random.randint(1,10)
    userguess=int(input("Enter a number between 1 to 10:"))
    if compguess==userguess:
        print("You won the game!!!!!!!")
        print(f":-) " * 10)
        break
    else:
        print("Wrong Choice")
        print(f":-( " * 10 )
        