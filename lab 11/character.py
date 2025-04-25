import abc

class Character(abc.ABC):

    @abc.abstractmethod
    def description(self):

        pass

    @abc.abstractmethod
    def magic_resistance(self):

        pass

    @abc.abstractmethod
    def strength(self):

        pass

    def __str__(self):

        return (f"Name: {self.description()}\n"
                f"MR: {self.magic_resistance()}\n"
                f"STR: {self.strength()}\n")