from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.c_capacity = 0
        self.c_memory = 0
        self.software_components = []
        self.light = 0
        self.express = 0

    def install(self, software: Software):
        if self.capacity >= software.capacity_consumption and self.memory >= software.memory_consumption:
            self.software_components.append(software)
            self.memory -= software.memory_consumption
            self.capacity -= software.capacity_consumption
            self.c_capacity += software.capacity_consumption
            self.c_memory += software.memory_consumption
            if software.__class__.__name__ == 'LightSoftware':
                self.light += 1
            else:
                self.express += 1
        else:
            return "Software cannot be installed"

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.c_capacity -= software.capacity_consumption
            self.c_memory -= software.memory_consumption
            self.memory += software.memory_consumption
            self.capacity += software.capacity_consumption
            if software.__class__.__name__ == 'LightSoftware':
                self.light -= 1
            else:
                self.express -= 1

    def __repr__(self):
        return self.name
