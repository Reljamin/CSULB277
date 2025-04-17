
import random
from entity import Entity

class ExpGoblin(Entity):
    def __init__(self):
        # Scarier name and increased HP range: 12-15
        hp = random.randint(12, 15)
        super().__init__("Horrible Goblin", hp)
    
    def melee_attack(self, enemy):
        # Damage range: 5-8
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return f"{self.name} bites {enemy.name} for {damage} damage."
