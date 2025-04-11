import pokemon
import random

class Fire(pokemon.Pokemon):
    def __init__(self, name=None):
        super().__init__(name if name else random.choice(["Ponyta", "Growlithe", "Vulpix"]), 0)

    def get_special_menu(self):
        return "1. Ember\n2. Fire Blast"

    def _special_move(self, opponent, move):
        # Determine effectiveness
        if opponent._poke_type == 1:  # Water
            dmg_multiplier = 0.5
            effect = "not very effective."
        elif opponent._poke_type == 2:  # Grass
            dmg_multiplier = 2
            effect = "SUPER EFFECTIVE!"
        else:  # Fire
            dmg_multiplier = 1
            effect = ""

        # Choose move and apply damage
        if move == 1:
            move_name = "EMBER"
            base_dmg = self._ember()
            attack_text = f"{self._name} scorches {opponent._name} with a burst of EMBER"
        else:
            move_name = "FIRE BLAST"
            base_dmg = self._fire_blast()
            attack_text = f"{self._name} engulfs {opponent._name} in a raging FIRE BLAST"

        total_dmg = int(base_dmg * dmg_multiplier)
        opponent._take_damage(total_dmg)

        return f"{attack_text} for {total_dmg} damage. {effect}"

    def _ember(self):
        return random.randint(2, 6)

    def _fire_blast(self):
        return random.randint(1, 7)
