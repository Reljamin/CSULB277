import random
from maze import Maze

class Ghost:
    def __init__(self):
        self._previous = '.'  # The character under the ghost before it moved

    def move(self):
        maze = Maze()
        ghost_pos = maze.search_maze('G')
        player_pos = maze.search_maze('P')

        gx, gy = ghost_pos #get ghost's x and y coordinates

        px, py = player_pos #get player's x and y coordinates

        # Determine movement direction toward player
        directions = []
        if px < gx:
            directions.append((-1, 0))  # up
        elif px > gx:
            directions.append((1, 0))   # down

        if py < gy:
            directions.append((0, -1))  # left
        elif py > gy:
            directions.append((0, 1))   # right

        # we put in all random directions just in case
        all_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(all_dirs) # shuffle them
        for d in all_dirs:
            if d not in directions:
                directions.append(d)

        
        for dr, dc in directions:
            nr, nc = gx + dr, gy + dc
            if maze.is_wall(nr, nc):
                continue

            
            maze.place_char(gx, gy, self.previous)
            self.previous = maze[nr][nc]
            maze.place_char(nr, nc, 'G')

            return self.previous == 'P'

        return False  