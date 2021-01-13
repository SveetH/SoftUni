class Software:
    def __init__(self, name: str, type: str, capacity_consumption: int, memory_consumption: int):
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value in ('Express', 'Light'):
            self._type = value

    def __repr__(self):
        return self.name
