from decorator import Decorator

class Ring(Decorator):
    def description(self):

        return "Ringed " + super().description()

    def magic_resistance(self):

        return super().magic_resistance() + 2

    def strength(self):

        return super().strength()