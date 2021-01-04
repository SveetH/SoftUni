class countdown_iterator():
    def __init__(self, count):
        self.count = count
        self.reverse_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverse_count <= self.count:
            number = self.count - self.reverse_count
            self.reverse_count += 1
            return number
        else:
            raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
