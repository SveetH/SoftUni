import unittest

from project.rooms.room import Room


class RoomTest(unittest.TestCase):

    def setUp(self):
        self.room = Room('Jones', 1450, 3)

    def test_init(self):
        self.assertEqual(self.room.family_name, 'Jones')
        self.assertEqual(self.room.budget, 1450)
        self.assertEqual(self.room.members_count, 3)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_expenses_with_negative_value(self):
        with self.assertRaises(ValueError) as cm:
            self.room.expenses = -20
        self.assertIsNotNone(cm.exception)

    def test_get_expenses_return_value(self):
        self.room.calculate_expenses([2, 3, 5], [3, 4])
        self.assertEqual(self.room.expenses, 17)


if __name__ == '__main__':
    unittest.main()
