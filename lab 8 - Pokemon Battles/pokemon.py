import check_input
import random
import abc

class Pokemon(abc.ABC):
    def __init__(self, name, p_type):
        self._name = name
        self._poke_type = p_type
        self._battle_table = [[1, 0.5, 2], [2, 1, 0.5], [0.5, 2, 1]]
        self._hp = 25

    @property
    def hp(self):
        return self._hp

    # Returns str
    def get_normal_menu(self):
        return "1. Slam\n2. Tackle"

    # Returns str
    def _normal_move(self, opponent, move):
        if move == 1:
            return self._slam(opponent)
        else:
            return self._tackle(opponent)

    # Returns str
    def _slam(self, opponent):
        dmg = random.randint(2, 6)
        opponent._take_damage(dmg)
        return f"{self._name} slams {opponent._name} for {dmg} damage."

    # Returns str
    def _tackle(self, opponent):
        dmg = random.randint(3, 5)
        opponent._take_damage(dmg)
        return f"{self._name} tackles {opponent._name} for {dmg} damage."

    # Abstract Methods
    @abc.abstractmethod
    def get_special_menu(self):
        pass

    @abc.abstractmethod
    def _special_move(self, opponent, move):
        pass

    # Returns str
    def attack(self, opponent, type, move):
        if type == 1:
            return self._normal_move(opponent, move)
        elif type == 2:
            return self._special_move(opponent, move)

    # Reduce HP but not below 0
    def _take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    # Returns str
    def __str__(self):
        return f"{self._name} HP: {self.hp}/25"
