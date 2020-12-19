class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError(f"Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        the_sum = 0
        for lis in args:
            for el in lis:
                the_sum += el.cost
        self.expenses = round(the_sum, 1) * 30
