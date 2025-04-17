import random
from entity import Entity

class BegTroll(Entity):

    def __init__(self):
        # HP range: 8-10
        hp = random.randint(8, 10)
        super().__init__("Troll", hp)
    
    def melee_attack(self, enemy):
        # damage range: 5-9
        damage = random.randint(5, 9)
        enemy.take_damage(damage)
        
        return f"{self.name} slams {enemy.name} for {damage} damage."
