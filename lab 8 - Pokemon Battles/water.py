import pokemon
import random

class Water(pokemon.Pokemon):
    def __init__(self, name=None):
        super().__init__(name if name else random.choice(["Staryu", "Magikarp", "Horsea"]), 1)  # Water-type = 1

    def get_special_menu(self):
        return "1. Water Gun\n2. Bubble Beam"

    def _special_move(self, opponent, move):
        # Determine effectiveness
        if opponent._poke_type == 2:  # Grass (Weak)
            dmg_multiplier = 0.5
            effect = "not very effective."
        elif opponent._poke_type == 0:  # Fire (Strong)
            dmg_multiplier = 2
            effect = "SUPER EFFECTIVE!"
        else:  # Water (Neutral)
            dmg_multiplier = 1
            effect = ""

        # Choose move and apply damage
        if move == 1:
            move_name = "WATER GUN"
            base_dmg = self._water_gun()
            attack_text = f"{self._name} blasts {opponent._name} with a stream of WATER GUN"
        else:
            move_name = "BUBBLE BEAM"
            base_dmg = self._bubble_beam()
            attack_text = f"{self._name} pelts {opponent._name} with a barrage of BUBBLE BEAM"

        total_dmg = int(base_dmg * dmg_multiplier)
        opponent._take_damage(total_dmg)

        return f"{attack_text} for {total_dmg} damage. {effect}"

    def _water_gun(self):
        return random.randint(1, 7)

    def _bubble_beam(self):
        return random.randint(3, 5)
