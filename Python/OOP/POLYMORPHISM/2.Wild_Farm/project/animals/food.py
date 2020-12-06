from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity

    # def __repr__(self):
    #     list_all = [self.__class__.__name__, self.quantity]
    #     return list_all


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)
