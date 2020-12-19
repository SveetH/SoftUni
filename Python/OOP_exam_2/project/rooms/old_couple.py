from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        self.room_cost = 15
        self.pension_one = pension_one
        self.pension_two = pension_two

        super().__init__(family_name, 0, 2)
        self.budget = self.pension_one + self.pension_two
        self.appliances = [TV(), Fridge(), Stove(), TV(), Fridge(), Stove()]
        self.children = []
        self.calculate_expenses(self.appliances)
