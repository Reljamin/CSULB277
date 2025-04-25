from decorator import Decorator

class Shield(Decorator):
    def description(self):

        return "Shielded " + super().description()

    def magic_resistance(self):

        return super().magic_resistance()

    def strength(self):

        return super().strength() + 2