import check_input # DONTG FORGET TO USE
import random


def display_board(board):
    
    for row in board:
        print()
        for tile in row:
            if tile == "S":
                print("~ ", end="")
            else:
                print(tile + " ", end="")
            
    print("\n")
    pass

def reset_game():
    arr = [
    [" ", "1", "2", "3", "4", "5"],
    ["A", "~", "~", "~", "~", "~"],
    ["B", "~", "~", "~", "~", "~"],
    ["C", "~", "~", "~", "~", "~"],
    ["D", "~", "~", "~", "~", "~"],
    ["E", "~", "~", "~", "~", "~"]
    ]

    shipTLC = [random.randint(1,4), random.randint(1,4)] # meaning the coordinates of the Ships Top Left Corncer

    arr[shipTLC[0]][shipTLC[1]] = "S"
    return arr

def get_row():

    pass

def fire_shot():

    pass


test = reset_game()
display_board(test)


