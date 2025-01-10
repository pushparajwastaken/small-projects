
import random
import time
def game(userinput,comp):
        
        if userinput == comp:
            print("It's a Draw")
            return 0
        elif (userinput==1 and comp==2) or (userinput==3 and comp==1) or (userinput==2 and comp==3):
            print(f"{name} won the round")
            return 1          
        else:
            print("Computer won this round")
            return -1     
print("Welcome to the Game of Snake,Water and Gun")
rounds=int(input("Enter the no. of rounds you want to play:"))
name=input("Enter your name:")

def playgame(rounds):
    compscore=0
    userscore=0
    print(f"{name} Let's start playing!!!!!")
    for i in range(rounds):  
            comp=random.randint(1,3)
            userinput=int(input("Enter 1 for Snake,2 for Water,3 for Gun: "))
            computerinput=print(f"Computer chose : {comp}")
            result=game(userinput,comp)
            if result==1:
                userscore+=1
            elif result==-1:
                compscore+=1
            print(f"Round {i+1}: {name}'s score : {userscore} Computer's Score: {compscore}")
            time.sleep(2)
    print(f"Final score:{name}'s Score:{userscore} Computer's Score:{compscore}")
    scores(compscore,userscore)

def scores(compscore,userscore):
    if compscore>userscore:
        print("Computer won this game")
    elif (userscore>compscore):
         print(f"Hurray {name}'s  won this round ")
    else:
        print("It's a Draw")
playgame(rounds)



 
