from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", capacity, memory)
        self.capacity *= 0.25
        self.memory *= 1.75
