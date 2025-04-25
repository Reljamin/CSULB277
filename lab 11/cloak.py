from decorator import Decorator

class Cloak(Decorator):
    def description(self):

        return "Cloaked " + super().description() 

    def magic_resistance(self):

        return super().magic_resistance() + 1

    def strength(self):

        return super().strength() + 1