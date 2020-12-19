from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        self.room_cost = 20
        self.salary_one = salary_one
        self.salary_two = salary_two

        super().__init__(family_name, 0, 2)
        self.budget = self.salary_one + self.salary_two
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        self.children = []
        self.calculate_expenses(self.appliances)


tv = TV()
fridge = Fridge()
laptop = Laptop()
