from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.room_cost = 30
        self.salary_one = salary_one
        self.salary_two = salary_two

        super().__init__(family_name, 0, 2)
        self.budget = self.salary_one + self.salary_two
        self.children = list(children)
        self.members_count = 2 + len(children)
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        for _ in range(len(self.children)):
            self.appliances += [TV(), Fridge(), Laptop()]
        self.calculate_expenses(self.appliances, children)


tv = TV()
fridge = Fridge()
laptop = Laptop()
