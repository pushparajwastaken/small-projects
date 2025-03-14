import time

# Checkpoints dictionary to store progress
checkpoints = {}

def save_checkpoint(name, stage):
    checkpoints[name] = stage

def load_checkpoint(name):
    return checkpoints.get(name, "start")

def game():
    print("Welcome to the Magical Adventure Game!")
    time.sleep(1)
    name = input("What is your name, brave adventurer? ").capitalize()
    stage = load_checkpoint(name)
    
    if stage == "start":
        print(f"Greetings, {name}! You find yourself in the Forbidden Forest, a mysterious place filled with magic, danger, and secrets.")
        time.sleep(1)
        print(f"Your quest is to find the legendary **Elder Wand**, hidden deep within the forest. This wand holds unimaginable power, but beware: many dangers lie ahead!")
        time.sleep(1)
        
        print("\nYou begin your journey at a crossroads. The path to your left is glowing faintly, while the one to your right is dark and ominous.")
        choice1 = input("Do you choose the **Glowing Path** or the **Dark Path**? (type 'Glowing' or 'Dark'): ").lower()
        
        if choice1 == "glowing":
            print("\nYou step onto the glowing path. The light grows brighter as you proceed, revealing a serene lake.")
            save_checkpoint(name, "glowing_path")
            stage = "glowing_path"
        elif choice1 == "dark":
            print("\nYou venture into the dark path. The forest grows colder, and eerie sounds surround you.")
            save_checkpoint(name, "dark_path")
            stage = "dark_path"
        else:
            print("\nInvalid choice. Game over!")
            return
    
    if stage == "glowing_path":
        print("Suddenly, a water spirit emerges and blocks your way. She says, 'To pass, you must prove your worth.'")
        choice1a = input("Do you **Bow Respectfully**, **Offer a Gift**, or **Ignore Her**? (type 'Bow', 'Gift', or 'Ignore'): ").lower()
        
        if choice1a == "bow":
            print("\nThe spirit smiles and grants you an enchanted orb. You move forward.")
            save_checkpoint(name, "ancient_ruin")
        elif choice1a == "gift":
            print("\nYou offer a token. The spirit grants you magical protection.")
            save_checkpoint(name, "ancient_ruin")
        else:
            print("\nThe spirit curses you. Game over!")
            return
    
    if stage == "dark_path":
        print("After a while, you encounter a group of goblins arguing over treasure.")
        choice1b = input("Do you **Eavesdrop**, **Confront Them**, or **Sneak Past**? (type 'Eavesdrop', 'Confront', or 'Sneak'): ").lower()
        
        if choice1b == "eavesdrop":
            print("\nYou learn that the goblins have a key. You take it and move on.")
            save_checkpoint(name, "ancient_ruin")
        elif choice1b == "confront":
            choice1b1 = input("Do you fight them with your wand (type 'Fight') or run away (type 'Run')? ").lower()
            if choice1b1 == "fight":
                print("\nYou defeat the goblins and take the key.")
                save_checkpoint(name, "ancient_ruin")
            else:
                print("\nThe goblins overwhelm you. Game over!")
                return
    
    if stage == "ancient_ruin":
        print("\nYou reach an ancient ruin with three doors:")
        print("1. 'The path of wisdom leads to enlightenment.'")
        print("2. 'The path of courage leads to glory.'")
        print("3. 'The path of greed leads to riches.'")
        choice2 = input("Which door do you choose? (type '1', '2', or '3'): ")

        if choice2 == "1":
            print("\nYou gain a powerful spell and move on.")
            save_checkpoint(name, "dragon_guardian")
        elif choice2 == "2":
            print("\nA basilisk blocks your way!")
            choice2a = input("Do you face it or sneak past? (type 'Face' or 'Sneak'): ").lower()
            if choice2a == "face":
                print("\nYou defeat the basilisk!")
                save_checkpoint(name, "dragon_guardian")
            else:
                print("\nThe basilisk strikes! Game over!")
                return
        elif choice2 == "3":
            print("\nYou take gold but trigger a trap!")
            save_checkpoint(name, "dragon_guardian")
    
    if stage == "dragon_guardian":
        print("\nThe Elder Wand lies ahead, guarded by a dragon!")
        choice3 = input("Do you **Negotiate**, **Fight**, or **Set a Trap**? (type 'Negotiate', 'Fight', or 'Trap'): ").lower()
        
        if choice3 == "negotiate":
            print("\nYou offer treasure or wisdom. The dragon lets you pass!")
        elif choice3 == "fight":
            print("\nThe dragon overpowers you. Game over!")
            return
        elif choice3 == "trap":
            print("\nYou cleverly trap the dragon and claim the Elder Wand!")
        print(f"\nCongratulations, {name}! You have triumphed!")

def play_game():
    print("Your magical journey awaits...")
    time.sleep(1)
    ques = input("Do you want to embark on the adventure? (yes or no): ").lower()
    if ques == "yes":
        game()
    else:
        print("Maybe next time! Farewell, adventurer.")

play_game()
