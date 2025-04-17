# ===========================
# Enemy Factory Interface (enemy_factory.py)
import abc

# ===========================
class EnemyFactory(abc.ABC):
    @abc.abstractmethod
    def create_random_enemy(self):
        pass

# =====================