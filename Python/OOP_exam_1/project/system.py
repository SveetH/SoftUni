from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []
    _total_memory = 0
    _total_capacity = 0
    _cur_memory = 0
    _cur_capacity = 0

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)
        System._total_capacity += hardware.capacity
        System._total_memory += hardware.memory

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)
        System._total_capacity += hardware.capacity
        System._total_memory += hardware.memory

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        find_name = [h for h in System._hardware if h.name == hardware_name]
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        if len(find_name) == 0:
            return "Hardware does not exist"
        elif len(find_name) != 0:
            hardware = find_name[0]
            if hardware.install(software) == "Software cannot be installed":
                return "Software cannot be installed"
            System._software.append(software)
            System._cur_capacity += software.capacity_consumption
            System._cur_memory += software.memory_consumption

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        find_name = [h for h in System._hardware if h.name == hardware_name]
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        if len(find_name) == 0:
            return "Hardware does not exist"
        elif len(find_name) != 0:
            hardware = find_name[0]
            if hardware.install(software) == "Software cannot be installed":
                return "Software cannot be installed"
            System._software.append(software)
            System._cur_capacity += software.capacity_consumption
            System._cur_memory += software.memory_consumption

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        find_hardware = [h for h in System._hardware if h.name == hardware_name]
        if len(find_hardware) == 0:
            return "Some of the components do not exist"
        hardware = find_hardware[0]
        find_software = [s for s in hardware.software_components if s.name == software_name]
        if len(find_software) == 0:
            return "Some of the components do not exist"
        software = find_software[0]
        System._cur_capacity -= software.capacity_consumption
        System._cur_memory -= software.memory_consumption
        hardware.uninstall(software)

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {System._cur_memory:.0f} / {System._total_memory:.0f}\n" \
               f"Total Capacity Taken: {System._cur_capacity:.0f} / {System._total_capacity:.0f}"

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            software_names = [s.name for s in hardware.software_components]
            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {hardware.express}\n" \
                      f"Light Software Components: {hardware.light}\n" \
                      f"Memory Usage: {hardware.c_memory:.0f} / {hardware.c_memory+hardware.memory:.0f}\n" \
                      f"Capacity Usage: {hardware.c_capacity:.0f}" \
                      f" / {hardware.c_capacity+hardware.capacity:.0f}\n" \
                      f"Type: {hardware.type}\n" \
                      f"Software Components: {', '.join(software_names)}\n"

        return result
