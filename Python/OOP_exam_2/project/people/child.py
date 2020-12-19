class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = toys_cost
        self.cost = 0

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        value = self.food_cost + sum(self.toys_cost)
        self._cost = value
