from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, horse_power, fuel):
        super().__init__(horse_power, fuel)

