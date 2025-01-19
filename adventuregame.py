import time

print("Welcome to the Magical Adventure Game!")

def game():
    print("The story begins...")
    time.sleep(1)
    name = input("What is your name, brave adventurer? ").capitalize()
    print(f"Greetings, {name}! You find yourself in the Forbidden Forest, a mysterious place filled with magic, danger, and secrets.")
    time.sleep(1)
    print(f"Your quest is to find the legendary **Elder Wand**, hidden deep within the forest. This wand holds unimaginable power, but beware: many dangers lie ahead!")
    time.sleep(1)

    print("\nYou begin your journey at a crossroads. The path to your left is glowing faintly, while the one to your right is dark and ominous.")
    choice1 = input("Do you choose the **Glowing Path** or the **Dark Path**? (type 'Glowing' or 'Dark'): ").lower()
    
    if choice1 == "glowing":
        print("\nYou step onto the glowing path. The light grows brighter as you proceed, revealing a serene lake.")
        time.sleep(1)
        print("Suddenly, a water spirit emerges and blocks your way. She says, 'To pass, you must prove your worth.'")
        choice1a = input("Do you **Bow Respectfully** or **Ignore Her**? (type 'Bow' or 'Ignore'): ").lower()
        
        if choice1a == "bow":
            print("\nThe spirit smiles and says, 'You have shown humility. Take this enchanted orb; it will guide you.' She vanishes, and you move forward with the orb.")
            time.sleep(1)
            print("The orb whispers directions as you continue deeper into the forest.")
        elif choice1a == "ignore":
            print("\nThe spirit becomes angry and conjures a whirlpool, dragging you into the lake. You drown. Game over!")
            quit()
        else:
            print("\nInvalid choice. The spirit curses you, and you lose your way. Game over!")
            quit()
    
    elif choice1 == "dark":
        print("\nYou venture into the dark path. The forest grows colder, and eerie sounds surround you.")
        time.sleep(1)
        print("After a while, you encounter a group of goblins arguing over treasure.")
        choice1b = input("Do you **Eavesdrop** on them or **Confront Them**? (type 'Eavesdrop' or 'Confront'): ").lower()
        
        if choice1b == "eavesdrop":
            print("\nYou quietly listen to their conversation. You learn that the goblins have a key to a hidden gate nearby.")
            time.sleep(1)
            print("You wait until they leave and take the key, continuing your journey.")
        elif choice1b == "confront":
            print("\nYou boldly step forward and demand the key. The goblins attack you!")
            choice1b1 = input("Do you fight them with your wand (type 'Fight') or run away (type 'Run')? ").lower()
            
            if choice1b1 == "fight":
                print("\nYou duel the goblins, casting powerful spells. You defeat them but suffer injuries. You take the key and move on.")
            elif choice1b1 == "run":
                print("\nYou try to run, but the goblins catch you. Game over!")
                quit()
            else:
                print("\nInvalid choice. The goblins overwhelm you. Game over!")
                quit()
        else:
            print("\nInvalid choice. You get lost in the darkness. Game over!")
            quit()
    
    else:
        print("\nInvalid choice. You stand still for too long and are ambushed by a forest troll. Game over!")
        quit()

    # Midpoint Challenge
    print("\nAfter overcoming the initial trials, you find yourself at an ancient ruin with three doors.")
    time.sleep(1)
    print("Each door has an inscription:")
    print("1. 'The path of wisdom leads to enlightenment.'")
    print("2. 'The path of courage leads to glory.'")
    print("3. 'The path of greed leads to riches.'")
    choice2 = input("Which door do you choose? (type '1', '2', or '3'): ")

    if choice2 == "1":
        print("\nYou enter a library filled with magical books. One book glows and whispers your name.")
        time.sleep(1)
        print("It grants you a powerful spell to use later. You feel wiser as you leave the library.")
    elif choice2 == "2":
        print("\nYou enter a chamber with a fierce basilisk guarding a treasure chest.")
        time.sleep(1)
        choice2a = input("Do you face the basilisk or try to sneak past it? (type 'Face' or 'Sneak'): ").lower()
        
        if choice2a == "face":
            print("\nYou bravely fight the basilisk, using the spell you learned earlier. You defeat it and claim the treasure!")
        elif choice2a == "sneak":
            print("\nYou try to sneak past, but the basilisk notices you and attacks. Game over!")
            quit()
        else:
            print("\nInvalid choice. The basilisk attacks you. Game over!")
            quit()
    elif choice2 == "3":
        print("\nYou enter a vault filled with gold and jewels. You take some riches, but a trap is triggered!")
        time.sleep(1)
        print("Poisonous gas fills the room, and you barely escape, losing valuable time.")
    else:
        print("\nInvalid choice. The ruins collapse around you. Game over!")
        quit()

    # Final Challenge
    print("\nFinally, you reach the heart of the Forbidden Forest. The Elder Wand lies on an altar, but a dragon guards it!")
    time.sleep(1)
    choice3 = input("Do you try to **Negotiate** with the dragon, **Fight** it, or **Set a Trap**? (type 'Negotiate', 'Fight', or 'Trap'): ").lower()
    
    if choice3 == "negotiate":
        print("\nYou speak to the dragon, offering it the treasure or wisdom you gained earlier.")
        time.sleep(1)
        print("The dragon accepts your offering and allows you to take the Elder Wand. You are victorious!")
        print(f"\nCongratulations, {name}! You have completed the Magical Adventure and obtained the Elder Wand!")
    elif choice3 == "fight":
        print("\nYou engage in a fierce battle with the dragon. Despite your efforts, the dragon is too powerful. Game over!")
        quit()
    elif choice3 == "trap":
        print("\nYou cleverly set a trap for the dragon, using the environment to your advantage. The dragon is subdued, and you claim the Elder Wand.")
        print(f"\nCongratulations, {name}! You have triumphed!")
    else:
        print("\nInvalid choice. The dragon incinerates you. Game over!")
        quit()

def play_game():
    print("Your magical journey awaits...")
    time.sleep(1)
    ques = input("Do you want to embark on the adventure? (yes or no): ").lower()
    if ques == "yes":
        game()
    else:
        print("Maybe next time! Farewell, adventurer.")
        quit()

play_game()
