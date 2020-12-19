class Appliance:
    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expense(self):
        cost_for_month = self.cost * 30
        return cost_for_month
