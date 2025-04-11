from maze import Maze

class Player:
    def move(self, direction):
        maze = Maze()  
        prev_pos = maze.search_maze('P')

        

        x, y = prev_pos
        new_x, new_y = x, y

        
        if direction == 'w':  
            new_x -= 1
        elif direction == 's': 
            new_x += 1
        elif direction == 'a':  
            new_y -= 1
        elif direction == 'd':  
            new_y += 1
        else:
            return False  

        # checks if you run into a wall
        if maze.is_wall(new_x, new_y):
            return False  

        # checks if you run into a ghost
        ran_into_ghost = maze[new_x][new_y] == 'G'

        # Move player
        maze.place_char(x, y, ' ')
        maze.place_char(new_x, new_y, 'P')

        return ran_into_ghost