from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.food_eaten = 0
        self.name = name
        self.weight = weight

    @abstractmethod
    def make_sound(self): pass

    @abstractmethod
    def feed(self, food): pass
