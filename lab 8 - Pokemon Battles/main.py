#@NickNojiri @Reljamin
import fire
import water
import grass
import random
import check_input  # Import input validation module

def main():
    """
    Pokémon battle game where the player picks 1 Pokémon, and the opponent has 3.
    - The player selects their Pokémon from Charmander, Squirtle, or Bulbasaur.
    - The opponent gets a random team of 3 Pokémon.
    - The player chooses which opponent to battle first.
    - The battle continues until all opponents are defeated or the player’s Pokémon faints.
    """

    # Generate a random team for the opponent
    all_pokemon = [
        fire.Fire("Ponyta"), fire.Fire("Growlithe"), fire.Fire("Vulpix"),
        water.Water("Horsea"), water.Water("Magikarp"), water.Water("Staryu"),
        grass.Grass("Oddish"), grass.Grass("Bellsprout"), grass.Grass("Exeggcute")
    ]
    
    opponent_team = random.sample(all_pokemon, 3)  # ✅ Picks 3 completely random Pokémon

    print("""PROF OAK: Hello Trainer! Today
you're off to fight your first
battle of 1 vs. 3 pokemon.""")

    for i, pokemon in enumerate(opponent_team, 1):
        print(f"{i}. {pokemon}")

    # Player chooses one Pokémon from the starters
    print("""Select the pokemon that you will
battle with.
1. I choose you, Charmander.
2. Squirtle! GO!
3. We can do it together,
Bulbasaur!
Please choose a pokemon: """, end="")

    player_choice = check_input.get_int_range("", 1, 3)
    if player_choice == 1:
        player_pokemon = fire.Fire("Charmander")
    elif player_choice == 2:
        player_pokemon = water.Water("Squirtle")
    else:
        player_pokemon = grass.Grass("Bulbasaur")

    print("-- TRAINER BATTLE --")

    while opponent_team and player_pokemon.hp > 0:
        current_opponent = opponent_team[0]

        print("\nTRAINER: I choose you:")
        print(f"{current_opponent}")
        print(f"{player_pokemon}")

        print("Choose an Attack Type:")
        print("1. Normal")
        print("2. Special")

        attack_type = check_input.get_int_range("Enter attack type: ", 1, 2)

        print("Choose a Move:")
        if attack_type == 1:
            print(player_pokemon.get_normal_menu())
        else:
            print(player_pokemon.get_special_menu())

        move_choice = check_input.get_int_range("Enter move: ", 1, 2)

        # Execute player's attack
        print(player_pokemon.attack(current_opponent, attack_type, move_choice))

        # Check if opponent is defeated
        if current_opponent.hp <= 0:
            print("TRAINER: NOOOOO! You defeated my pokemon!")
            opponent_team.pop(0)

            if not opponent_team:
                print("You won the battle!")
                return

        # Opponent's turn if still alive
        if opponent_team:
            print(opponent_team[0].attack(player_pokemon, random.randint(1, 2), random.randint(1, 2)))

    print("TRAINER: HA! I defeated you, come back when you get a better pokemon...")

if __name__ == "__main__":
    main()
