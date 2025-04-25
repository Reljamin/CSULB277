'''
Names: nick nojiri & ariel winkler
Date: 4/24/2025
Description: Decorator class creation and battling project




'''
from bard import Bard
from warrior import Warrior
from wizard import Wizard
from cloak import Cloak
from ring import Ring
from shield import Shield
import check_input
import random

def main():

    print("Character Maker!")
    print("Choose a starting character:\n")

    print("1. Bard")
    print("2. Warrior")
    print("3. Wizard")

    userChoice = check_input.get_int_range("> ", 1, 3)

    if userChoice == 1:
        character = Bard()
    elif userChoice == 2:
        character = Warrior()
    elif userChoice == 3:
        character = Wizard()

    print(character)

    items = ["Sturdy Shield", "Magic Ring", "Protective Cloak"]
    for i in range(2):
        print("Choose " + str(2-i) + " items:")

        for i in range(len(items)):
            print(str(i + 1) + ". " + items[i])
        
        

        itemChoice = check_input.get_int_range("> ", 1, len(items)) - 1

        if items[itemChoice] == "Sturdy Shield":
            character = Shield(character)
        elif items[itemChoice] == "Magic Ring":
            character = Ring(character)
        elif items[itemChoice] == "Protective Cloak":
            character = Cloak(character)

        items.pop(itemChoice)
        print("")
        print(character)
    

    monsters = [
        {"name": "Spiked Dragon", "magic": 0, "strength": 6},
        {"name": "Orc Warlord", "magic": 1, "strength": 5},
        {"name": "Shadow Knight", "magic": 2, "strength": 4},
        {"name": "Lava Monster", "magic": 3, "strength": 3},
        {"name": "Fiendish Ghoul", "magic": 4, "strength": 2},
        {"name": "Goblin Mage", "magic": 5, "strength": 1},
        {"name": "Dark Magician", "magic": 6, "strength": 0}
    ]

    print("You must pass two of the following three trials!\n")

    trialMonsters = random.sample(monsters, 3)
    trialsPassed = 0
    trialsFailed = 0
    trialIndex = 0

    while trialIndex < 3 and trialsFailed < 2:
        monster = trialMonsters[trialIndex]
        print(f"Trial {trialIndex + 1}: A wild {monster['name']} appears!")
        print(f"MR: {monster['magic']}   \nSTR: {monster['strength']}")

        print("")
        print("1. Battle")
        print("2. Dodge")

        battleChoice = check_input.get_int_range("> ", 1, 2)
        print("")

        if battleChoice == 1:
            if character.magic_resistance() >= monster["magic"] and character.strength() >= monster["strength"]:
                print(f"You battle with the {monster['name']} and easily defeat it.\n")
                trialsPassed += 1
            else:
                print(f"You were overpowered by the {monster['name']} and failed this trial.\n")
                trialsFailed += 1
        else:
            if random.randint(1, 4) == 1:
                print(f"You successfully dodged the {monster['name']}\n")
                trialsPassed += 1
            else:
                print(f"You attempt to dodge the {monster['name']}, but it manages to hit you. You have failed this trial.\n")
                trialsFailed += 1

        trialIndex += 1

    if trialsPassed >= 2:
        print("You passed at least two trials. You win!")
    else:
        print("You failed too many trials. You lose")

if __name__ == "__main__":
    main()