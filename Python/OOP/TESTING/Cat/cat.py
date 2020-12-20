class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class Ass(object):
    def __init__(self, name, age: int):
        self.name = name
        self.age = age * 2

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        if not type(value) == int:
            raise ValueError("incorrect")

    def get_dict(self):
        return Ass.__dict__

    @staticmethod
    def calc():
        return 4 * 5

    def __repr__(self):
        return self.name


ass = Ass("ass", 4)
print(ass.age)
the_dict = ass.get_dict()

[print(f"{k} ------ {v}\n") for k, v in the_dict.items()]
