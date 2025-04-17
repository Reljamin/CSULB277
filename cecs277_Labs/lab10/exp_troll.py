import random
from entity import Entity

class ExpTroll(Entity):
    def __init__(self):
        # Scarier name and increased HP range: 15-18
        hp = random.randint(15, 18)
        super().__init__("Angry Troll", hp)
    
    def melee_attack(self, enemy):
        # Damage range: 8-12
        damage = random.randint(8, 12)
        enemy.take_damage(damage)
        return f"{self.name} slams {enemy.name} for {damage} damage."