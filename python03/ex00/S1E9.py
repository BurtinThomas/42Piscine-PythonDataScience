from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, is_alive = True):
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass

class Stark(Character):
    def __init__(self, name, is_alive = True):
        super().__init__(name, is_alive)
    
    def die(self):
        self.is_alive = False

