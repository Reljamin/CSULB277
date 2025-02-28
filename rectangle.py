'''
Names: nick nojiri & ariel winkler
Date: 2/27/2025
Description: square class to be moved on a 20x20 grid
'''

class Rectangle:
    """ 
    Represents a rectangle on the grid.
    Attributes:
            x (int): x value of the top left of the rectangle.
            y (int): y value of the top left of the rectanle.
            width (int): width value of the rectangle.
            height (int): height value of the rectangle.
    """
    def __init__(self, w, h):
        """ sets the values of x, y, width, and height """
        self.x = 0
        self.y = 0
        self.width = w
        self.height = h

    def get_coords(self):
        """ returns the coordinates of the rectanlge """
        return self.x, self.y
    
    def get_dimensions(self):
        """ returns the dimensions of the rectanlge """
        return self.width, self.height
    
    def move_up(self):
        """ moves the rectangle up"""
        self.x -= 1

    def move_down(self):
        """ moves the rectangle down"""
        self.x += 1

    def move_right(self):
        """ moves the rectangle right"""
        self.y += 1

    def move_left(self):
        """ moves the rectangle left"""
        self.y -= 1