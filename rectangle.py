class Rectangle:
    def __init__(self, w, h):
        self.x = 0
        self.y = 0
        self.width = w
        self.height = h

    def get_coords(self):
        return self.x, self.y
    
    def get_dimensions(self):
        return self.width, self.height
    
    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1