import player
import check_input

def take_turn(player):

    

    player.roll_dice()

    print("\n" + str(player))

    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
        
    elif player.has_pair():
        print("You got a pair!")
        
    elif player.has_series():
        print("You got a series of 3!")
        

    print("score = " + str(player.points()))

    



def main():

    user = player.Player()
    keepPlaying = True

    print("-Yahtzee-")

    while (keepPlaying):
        
        take_turn(user)
        keepPlaying = check_input.get_yes_no("Play again? (Y/N):")

    print("\nGame Over.\nFinal Score = " + str(user.points()))


main()