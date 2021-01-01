import unittest

from cat import Cat


class CatTest(unittest.TestCase):

    def test_if_the_cats_size_increase_when_eat_method_is_called(self):
        name = 'Mike'
        cat_1 = Cat(name)
        cat_1.eat()

        self.assertEqual(cat_1.size, 1)

    def test_if_the_fed_attr_is_equel_to_true_when_eat_method_is_called(self):
        name = 'Mike'
        cat_1 = Cat(name)
        cat_1.eat()
        self.assertEqual(cat_1.fed, True)

    def test_if_error_value_is_raised_when_fed_attr_is_set_to_true_and_call_eat_method_again(self):
        name = 'Mike'
        cat_1 = Cat(name)
        cat_1.eat()
        with self.assertRaises(Exception) as cm:
            cat_1.eat()
        self.assertIsNotNone(cm.exception)

    def test_if_error_value_is_raised_when_sleep_method_and_attr_fed_equel_to_false(self):
        name = 'Mike'
        cat_1 = Cat(name)
        with self.assertRaises(Exception) as cm:
            cat_1.sleep()
        self.assertIsNotNone(cm.exception)

    def test_5(self):
        name = 'Mike'
        cat_1 = Cat(name)
        cat_1.eat()
        cat_1.sleep()
        self.assertFalse(cat_1.sleepy)


if __name__ == '__main__':
    unittest.main()


