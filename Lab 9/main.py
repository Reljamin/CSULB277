# main.py
from maze import Maze
from player import Player
from ghost import Ghost

def main():
    
    maze = Maze()
    player = Player()
    ghost = Ghost()

    while True:
        # show the maze
        print(maze)

        
        if maze.count_dots() == 0:

            print("you win!")
            break #breaks us out of our while loop

        
        direction = input("Enter direction (w = up, a = left, s = down, d = right): ").lower()

        if direction not in ['w', 'a', 's', 'd']:

            print("please choose either: w, a, s, or d.")
            continue #skips the rest of the code and keeps the loop going which basically asks the user for input again

        
        ran_into_ghost = player.move(direction)

        if ran_into_ghost:
            print(maze)
            print("you ran into the ghost and lost!")
            break #breaks us out of our while loop

        
        if maze.is_wall(*maze.search_maze('P')):
            print("you hit a wall but the ghost still moved")

        # call the ghost move to move it, if it returns true then 
        if ghost.move():
            print(maze)
            print("The ghost caught you! You lose!")
            break

        
        print("\n")

if __name__ == "__main__":
    main()
