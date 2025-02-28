'''
Names: nick nojiri & ariel winkler
Date: 2/27/2025
Description: moving square on a 20x20 grid program
'''

import check_input
import rectangle

def display_grid(grid):
    """ displays the 20x20 grid of dots and the rectangle """
    for row in grid:
        for item in row:
            print(item, end="")
        print()

def reset_grid(grid):
    """ resets the grid to only have dots """

    for i in range(20):
        for j in range(20):
            grid[i][j] = "."
                
        
        

    return grid


def place_rect(grid, rect):
    """ places the rectangle on the grid represented with asterisks """
    x, y = rect.get_coords()
    w, h = rect.get_dimensions()

    for i in range(w):
        for j in range(h):
            grid[i + x][j + y] = "*"

    return grid

def main():

    
    w = check_input.get_int_range("Enter rectangle width (1-5): ", 1, 5)
    h = check_input.get_int_range("Enter rectangle height (1-5): ", 1, 5)
    
    grid = []
    for  i in range(20):
        list = []
        for j in range(20):
            list.append(".")
        grid.append(list)
    
    rect = rectangle.Rectangle(h, w)
    place_rect(grid, rect)
    display_grid(grid)
    
    userChoice = 0
    while (userChoice != 5):
        userChoice = check_input.get_int_range("Enter Direction: \n1. Up\n2. Down\n3. Left\n4. Right\n5. Quit\n", 1, 5)

        if userChoice == 1:

            if rect.get_coords()[0] == 0:
                print("Out of bounds")
            else:
                
                rect.move_up()
                reset_grid(grid)
                place_rect(grid, rect)
                display_grid(grid)
            
        if userChoice == 2:

            if rect.get_coords()[0] + rect.get_dimensions()[0] == 20:
                print("Out of bounds")
            else:
                rect.move_down()
                reset_grid(grid)
                place_rect(grid, rect)
                display_grid(grid)

            
        if userChoice == 3:

            if rect.get_coords()[1] == 0:
                print("Out of bounds")
                
            else:
                
                rect.move_left()
                reset_grid(grid)
                place_rect(grid, rect)
                display_grid(grid)

            
        if userChoice == 4:

            if rect.get_coords()[1] + rect.get_dimensions()[1] == 20:
                print("Out of bounds")
            else:
                rect.move_right()
                reset_grid(grid)
                place_rect(grid, rect)
                display_grid(grid)
                    

        

main()
        
