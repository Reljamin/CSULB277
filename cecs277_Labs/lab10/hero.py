
import random
from entity import Entity

class Hero(Entity):
    def __init__(self, name):
        # default hp of 25.
        super().__init__(name, 25)
    
    def melee_attack(self, enemy):
        # Two six sided dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        damage = die1 + die2
        enemy.take_damage(damage)
        return f"{self.name} slashes {enemy.name} with a sword for {damage} damage."
    
    def ranged_attack(self, enemy):
        # One 12 sided die
        damage = random.randint(1, 12)
        enemy.take_damage(damage)
        return f"{self.name} pierces {enemy.name} with an arrow for {damage} damage."
