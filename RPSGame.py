'''
Names: Nick Nojiri & Ariel Winkler
Date: 2/6/2025
Description: A rock paper scizzors game against the computer that tracks the score.




'''

# Import required modules
import random
import check_input

# ----------------------------------------
# Function 1: Display the weapon menu and get user input
# ----------------------------------------
def weapon_menu():
    """
    Displays the weapon menu and prompts the user to choose a weapon.
    Validates the input and returns the user's choice (R, P, S, or B).
    """
    # Step 1: Display the menu options
    print("Choose your weapon: ")
    print("R. Rock \nP. Paper \nS. Scizzors \nB. Back")
    
    # Step 2: Use a loop to validate the user's input
    user_weapon = "N"
    while (user_weapon == "N"):
        user_weapon = input()
        if user_weapon.upper() not in ["R", "P", "S", "B"]:
            user_weapon = "N"
            print("Invalid Input - Choose Again")
            print("R. Rock \nP. Paper \nS. Scizzors \nB. Back")
        


    # Step 3: Return the valid choice
    if user_weapon.upper() == "R":
        print("You chose Rock")
    elif user_weapon.upper() == "P":
        print("You chose Paper")
    elif user_weapon.upper() == "S":
        print("You chose Scizzors")
    
    return user_weapon.upper()

#weapon_menu()
# ----------------------------------------
# Function 2: Generate the computer's weapon choice
# ----------------------------------------
def comp_weapon():
    """
    Randomly selects the computer's weapon (R, P, or S) and returns it.
    """
    # Step 1: Use the random module to generate a number (1, 2, or 3)

    computer_input = random.randint(1,3)

    # Step 2: Map the number to a weapon (R, P, or S)

    weapon_dict = {
        1: "R",
        2: "P",
        3: "S"
    }

    # Step 3: Return the computer's choice
    
    #print(weapon_dict[computer_input])
    return weapon_dict[computer_input]

# ----------------------------------------
# Function 3: Determine the winner
# ----------------------------------------
def find_winner(player, comp):
    """
    Compares the player's and computer's choices to determine the winner.
    Returns:
    0 for a tie,
    1 for a player win,
    2 for a computer win.
    """

    if player == "B":
        return

    # Step 1: Use conditional statements to compare the choices
    winner = -1
    if player == comp:
        winner = 0
        print("Tie")
    elif (player == "R" and comp == "S") or (player == "S" and comp == "P") or (player == "P" and comp == "R"):
        winner = 1
        print("Player wins")
    else:
        winner = 2
        print("Computer wins")

    # Step 2: Return the result (0, 1, or 2)

    return winner
    pass # Replace with your code
# ----------------------------------------
# Function 4: Display the scores
# ----------------------------------------
def display_scores(player, comp):
    """
    Displays the player's and computer's scores.
    """
    # Step 1: Print the player's score
    print("Player = " + str(player))
    # Step 2: Print the computer's score
    print("Computer = " + str(comp))
    pass # Replace with your code
# ----------------------------------------
# Main Function: Run the game
# ----------------------------------------
def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    """
    # Step 1: Initialize variables for player and computer scores
    player_points = 0
    comp_points = 0
    # Step 2: Use a loop to display the main menu and handle user choices
    while True:
        # Display the main menu and get the user's choice
        print("RPS Menu:")
        print("1. Play Game")
        print("2. Show Score")
        print("3. Quit")
        choice = input("Enter your choice: ")
        # Handle the user's choice
        if choice == "1":
            # Step 3: Play the game
            playingGame = True
            while playingGame:

            # - Get the player's weapon choice
                player_choice = weapon_menu()
                # - Get the computer's weapon choice
                computer_choice = comp_weapon()
                
                if player_choice != "B":
                    if computer_choice == "R":
                        print("Computer chose Rock")
                    elif computer_choice == "P":
                        print("Computer chose Paper")
                    elif computer_choice == "S":
                        print("Computer chose Scizzors")
                    winner = find_winner(player_choice, computer_choice)
                    # - Update the scores
                    if winner == 1:
                        player_points += 1
                    if winner == 2:
                        comp_points += 1
                else:
                    playingGame = False

            # - Determine the winner
            #print(player_choice)
            #print(computer_choice)
            
            
        elif choice == "2":
            # Step 4: Display the scores
            display_scores(player_points, comp_points)
            
        elif choice == "3":
            # Step 5: Quit the game and display the final scores
            print("Final Score:")
            display_scores(player_points, comp_points)
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")
# ----------------------------------------
# Run the program
# ----------------------------------------
if __name__ == "__main__":
   main()
