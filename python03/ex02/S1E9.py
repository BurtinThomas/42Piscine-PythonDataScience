from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, first_name, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass
    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    def __repr__(self):
        return self.__str__()

class Stark(Character):
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name, is_alive)
    def die(self):
        self.is_alive = False

