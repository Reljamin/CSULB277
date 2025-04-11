from maze import Maze

class Player:
    def move(self, direction):
        maze = Maze()  
        prev_pos = maze.search_maze('P')

        

        r, c = prev_pos
        new_r, new_c = r, c

        
        if direction == 'w':  # Up
            new_r -= 1
        elif direction == 's':  # Down
            new_r += 1
        elif direction == 'a':  # Left
            new_c -= 1
        elif direction == 'd':  # Right
            new_c += 1
        else:
            return False  # Invalid direction, do nothing

        # Check for wall
        if maze.is_wall(new_r, new_c):
            return False  # Player stays in the same place

        # Check if moving into ghost
        ran_into_ghost = maze[new_r][new_c] == 'G'

        # Move player
        maze.place_char(r, c, ' ')
        maze.place_char(new_r, new_c, 'P')

        return ran_into_ghost