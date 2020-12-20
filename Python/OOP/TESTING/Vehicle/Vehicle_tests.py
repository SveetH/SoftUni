import unittest

from vehicle import Car, Truck


class VehicleTest(unittest.TestCase):

    def test_1(self):
        fuel_quantity = 50
        fuel_consumption = 2
        car = Car(fuel_quantity, fuel_consumption)
        car.refuel(50)
        self.assertEqual(car.fuel_quantity, 100)

    def test_2(self):
        fuel_quantity = 80
        fuel_consumption = 2
        distance = 25
        expect_result = fuel_quantity - (fuel_consumption + 0.9) * distance
        car = Car(fuel_quantity, fuel_consumption)
        car.drive(distance)
        self.assertEqual(car.fuel_consumption, fuel_consumption + 0.9)
        self.assertEqual(car.fuel_quantity, expect_result)

    def test_3(self):
        fuel_quantity = 50
        fuel_consumption = 2
        truck = Truck(fuel_quantity, fuel_consumption)
        truck.refuel(50)
        self.assertEqual(truck.fuel_quantity, 50 + 50 * 0.95)

    def test_4(self):
        fuel_quantity = 50
        fuel_consumption = 2
        distance = 3
        expect_result = fuel_quantity - (fuel_consumption + 1.6) * distance
        truck = Truck(fuel_quantity, fuel_consumption)
        truck.drive(distance)
        self.assertEqual(truck.fuel_consumption, fuel_consumption + 1.6)
        self.assertEqual(truck.fuel_quantity, expect_result)


if __name__ == '__main__':
    unittest.main()
