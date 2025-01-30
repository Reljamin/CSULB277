import check_input
import random

def three_card_monte( bank ):
    print("You have $" + str(bank) + ".")
    bet = check_input.get_int_range("How much you wanna bet? ", 0, bank)
    winner = random.randrange(1,3,1)
    display_cards(winner, False)
    guess = check_input.get_int_range("Find the queen: ", 1, 3)

    
    display_cards(winner, True)
    if guess == winner:
        print("You got lucky this time...\n")
        bank += bet*2
    else:
        print("Sorry... you lose.")
        bank -= bet
    return bank

       

def display_cards( winner, reveal = False):
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
    bank = 100
    reroll = True
    print("-Three Card Monte-\nFind the queen to double your bet!\n")
    while (reroll == True) and (bank > 0):
        bank = three_card_monte(bank)
        if bank > 0:
            reroll = check_input.get_yes_no("Play again? (Y/N)\n")
        else:
            print("You're out of Money.  Beat it\nloser!")

if __name__ == "__main__":
    main()
