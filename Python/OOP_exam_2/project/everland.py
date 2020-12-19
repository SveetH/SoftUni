from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumption = 0
        for room in self.rooms:
            monthly_consumption += room.room_cost + room.expenses
        return f"Monthly consumption: {monthly_consumption:.2f}$."

    def pay(self):
        string = ""
        for room in self.rooms:
            monthly_consumption = 0
            monthly_consumption += room.room_cost + room.expenses
            if room.budget >= monthly_consumption:
                string += f"{room.family_name} paid {monthly_consumption:.2f}$ and have {room.budget:.2f}$ left.\n"
                room.budget -= monthly_consumption
            else:
                string += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return string

    def status(self):
        string = ""
        total_pop = 0
        for room in self.rooms:
            total_pop += room.members_count
        string += f"Total population: {total_pop}\n"
        for room in self.rooms:
            monthly_consumption = 0
            # children = [child.cost for child in room.children]
            # room.calculate_expenses([el * room.members_count for el in room.appliances], children)
            monthly_consumption += room.expenses
            # curr = room.budget - monthly_consumption - room.room_cost
            string += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$," \
                      f" Expenses: {monthly_consumption:.2f}$\n"
            if len(room.children) > 0:
                for i in range(len(room.children)):
                    children = [child.cost for child in room.children]
                    string += f"--- Child {i + 1} monthly cost: {children[i] * 30:.2f}$\n"
            if len(room.appliances) > 0:
                room.calculate_expenses(room.appliances)
                string += f"--- Appliances monthly cost: {room.expenses :.2f}$\n"
        return string
