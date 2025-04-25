import abc
from character import Character

class Decorator(Character, abc.ABC):
    
    def __init__(self, c):
        self._character = c

    def description(self):

        return self._character.description()

    def magic_resistance(self):

        return self._character.magic_resistance()

    def strength(self):
        
        return self._character.strength()
