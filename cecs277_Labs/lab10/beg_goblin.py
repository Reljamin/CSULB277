import random
from entity import Entity


class BegGoblin(Entity):
    def __init__(self):
        # HP range: 7-9
        hp = random.randint(7, 9)
        super().__init__("Goblin", hp)
    
    def melee_attack(self, enemy):
        # Damage range: 4-6
        damage = random.randint(4, 6)
        enemy.take_damage(damage)
        return f"{self.name} bites {enemy.name} for {damage} damage."


