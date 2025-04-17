
import check_input
from hero import Hero
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory

def main():
    print("Monster Trials")
    hero_name = input("What is your name? ")
    hero = Hero(hero_name)
    print(f"\nYou will face a series of 3 monsters, {hero.name}.")
    print("Defeat them all to win.\n")

    # Create factories
    beginner_factory = BeginnerFactory()
    expert_factory = ExpertFactory()

    # Generate monsters
    monsters = [
        beginner_factory.create_random_enemy(),
        beginner_factory.create_random_enemy(),
        expert_factory.create_random_enemy()
    ]

    # main game loop
    while hero.hp > 0 and monsters:
        print("\nChoose an enemy to attack:")
        for i, monster in enumerate(monsters, start=1):
            print(f"{i}. {monster}")
        
        # validate enemy selection using check_input's get_int_range
        choice = check_input.get_int_range("Enter choice: ", 1, len(monsters))
        current_monster = monsters[choice - 1]

        # show hero's current hp and choose type of attack
        print(f"\n{hero.name} HP: {hero.hp}")
        print("1. Sword Attack")
        print("2. Arrow Attack")
        attack_choice = check_input.get_int_range("Enter choice: ", 1, 2)

        # hero's attack
        if attack_choice == 1:
            attack_result = hero.melee_attack(current_monster)
        else:
            attack_result = hero.ranged_attack(current_monster)
        print(attack_result)

        # if the enemy is still alive let them attack back
        if current_monster.hp > 0:
            enemy_attack = current_monster.melee_attack(hero)
            print(enemy_attack)
        else:
            print(f"You have slain the {current_monster.name}!")
            monsters.remove(current_monster)

        # show current hero hp
        print(f"{hero.name} HP: {hero.hp}")
        if hero.hp <= 0:
            print(f"\n{hero.name} has been defeated!")
            break

    # game outcome
    if hero.hp > 0 and not monsters:
        print("\nCongratulations! You defeated all three monsters!")
    print("Game Over.")

if __name__ == "__main__":
    main()