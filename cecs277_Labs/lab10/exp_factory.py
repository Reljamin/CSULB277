import random
from enemy_factory import EnemyFactory  # For the base factory class
from exp_goblin import ExpGoblin        # To create an expert goblin
from exp_troll import ExpTroll          # To create an expert troll


class ExpertFactory(EnemyFactory):

    def create_random_enemy(self):
        enemy_class = random.choice([ExpGoblin, ExpTroll])
        
        return enemy_class()
