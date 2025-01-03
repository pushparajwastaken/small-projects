print("Welcome to the game")

def game():
    name=input("What is your Name?")
    print(f"Let's Play {name}")
    print(f"{name} is in the middle of the forest.He has to find a a wise man and get a map to leave this place.There are two ways in front of him")
    choice1=input("Type Left to go left or Right to go right or Q for quit: ").lower()
    if choice1=="q":
        quit
    elif choice1=="right":
        print("You go right and after walking for 5 minutes you came across a river")
        choice1a=input("You can choose to swim throught it or go across.Press Swim to swim or Walk to get across: ").lower()
        if choice1a=="swim":
            print("You swam,There were crocodiles in the river,They ate you and you died :-(")
            quit
        elif choice1a=="walk":
            print("You walked across the river ,You walked for several miles and couldn't find the old man ,Your supplies finished and You lost the game :-(")
            quit
        else:
            print("Invalid Answer")
    elif choice1=="left":
        print("You chose left ,You walked for 10 minute and came across a woobly bridge")
        choice1b=input("You can walk acorss it or go back.Press Walk to go through or Back to go Back: ").lower()
        if choice1b=="back":
            print("You are not Brave.You Lost the Game!!!!!! :-0")
        elif choice1b=="walk":
            print("You Bravely crossed the bridge and then walked straight and found the old wise man who gave you the map")
            print(f"\n Congratulations!!!!! {name} won the Game :-)")
            print(f"#" * 15 )
        else:
            print("Invalid Syntax")
    else:
        print("Invalid Syntax")
def playgame():
    ques=input("Do you want to play the Game?").lower()
    if ques!="yes":
        quit
    else:
        game()

playgame()