import random
import abc
import check_input  # Assumes you have check_input-7.py available as check_input


class Entity(abc.ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    def take_damage(self, dmg):
        self._hp = max(self._hp - dmg, 0)

    def __str__(self):
        return f"{self.name} HP: {self.hp}"

    @abc.abstractmethod
    def melee_attack(self, enemy):
        pass
