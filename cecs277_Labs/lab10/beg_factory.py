

import random
from enemy_factory import EnemyFactory  # For the base factory class
from beg_goblin import BegGoblin       # To create a beginner goblin
from beg_troll import BegTroll         # To create a beginner troll

class BeginnerFactory(EnemyFactory):

    def create_random_enemy(self):

        enemy_class = random.choice([BegGoblin, BegTroll])
        
        return enemy_class()