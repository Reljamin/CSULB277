'''
Names: nick nojiri & ariel winkler
Date: 1/30/2025
Description: Three card monte




'''


import check_input
import random





def three_card_monte( bank ):
    """the main game, asks you how much you want to bet and to choose a card. bank is how much money you have. we return bank acting as our balance."""
    print("You have $" + str(bank) + ".")

    #checks for validation
    bet = check_input.get_int_range("How much you wanna bet? ", 1, bank)
    winner = random.randrange(1,3,1)
    display_cards(winner, False)
    guess = check_input.get_int_range("Find the queen: ", 1, 3)

    
    display_cards(winner, True)


    if guess == winner:
        print("You got lucky this time...\n")
        bank += bet
    else:
        print("Sorry... you lose.")
        bank -= bet
    return bank

       

def display_cards( winner, reveal = False):
    """ASCII art for the cards, winner is a parameter for the winning card, reveal is a bolean for if the cards are shown or hidden."""
    if not reveal:
        cards = "+-----+ +-----+ +-----+\n" \
                "|     | |     | |     |\n" \
                "|  1  | |  2  | |  3  |\n" \
                "|     | |     | |     |\n" \
                "+-----+ +-----+ +-----+"
    else:
        card1 = 'K'
        card2 = 'K'
        card3 = 'K'
        #nested if statement to check which card is the queen
        if winner == 1:
            card1 = 'Q'
        elif winner == 2:
            card2 = 'Q'
        else:
            card3 = 'Q'
        cards = "+-----+ +-----+ +-----+\n" \
                "|     | |     | |     |\n" \
                "|  "+ card1 +"  | |  "+ card2 +"  | |  "+ card3 +"  |\n" \
                "|     | |     | |     |\n" \
                "+-----+ +-----+ +-----+"
    print(cards)
    

def main():
    """ the gameplay loop """
    bank = 100
    reroll = True
    print("-Three Card Monte-\nFind the queen to double your bet!\n")

    #if player chose to play again and has enough money call game function
    while (reroll == True) and (bank > 0):
        bank = three_card_monte(bank)
        if bank > 0:
            reroll = check_input.get_yes_no("Play again? (Y/N)\n")
        else:
            print("You're out of Money.  Beat it\nloser!")

if __name__ == "__main__":
    main()
