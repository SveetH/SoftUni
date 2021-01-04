class take_skip():
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            self.current += 1
            number = self.number
            self.number += self.step
            return number
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print('\n')

numbers = take_skip(10, 5)
for number in numbers:
    print(number)


# li = [23, 32, 32, 32, ]
#
# list_iter = iter(li)
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
