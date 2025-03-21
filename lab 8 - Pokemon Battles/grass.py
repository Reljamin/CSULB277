import pokemon
import random

class Grass(pokemon.Pokemon):
    def __init__(self, name=None):
        super().__init__(name if name else random.choice(["Oddish", "Bellsprout", "Exeggcute"]), 2)  # Grass-type = 2

    def get_special_menu(self):
        return "1. Razor Leaf\n2. Solar Beam"

    def _special_move(self, opponent, move):
        # Determine effectiveness
        if opponent._poke_type == 0:  # Fire (Weak)
            dmg_multiplier = 0.5
            effect = "not very effective."
        elif opponent._poke_type == 1:  # Water (Strong)
            dmg_multiplier = 2
            effect = "SUPER EFFECTIVE!"
        else:  # Grass (Neutral)
            dmg_multiplier = 1
            effect = ""

        # Choose move and apply damage
        if move == 1:
            move_name = "RAZOR LEAF"
            base_dmg = self._razor_leaf()
            attack_text = f"{self._name} slices {opponent._name} with RAZOR sharp LEAVES"
        else:
            move_name = "SOLAR BEAM"
            base_dmg = self._solar_beam()
            attack_text = f"{self._name} blasts {opponent._name} with a powerful SOLAR BEAM"

        total_dmg = int(base_dmg * dmg_multiplier)
        opponent._take_damage(total_dmg)

        return f"{attack_text} for {total_dmg} damage. {effect}"

    def _razor_leaf(self):
        return random.randint(3, 5)

    def _solar_beam(self):
        return random.randint(2, 6)
