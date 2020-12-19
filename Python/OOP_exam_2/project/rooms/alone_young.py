from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        self.room_cost = 10
        self.salary = salary
        super().__init__(family_name, 0, 1)
        self.budget = self.salary
        self.appliances = [tv, ]
        self.children = []
        self.calculate_expenses(self.appliances)


tv = TV()
