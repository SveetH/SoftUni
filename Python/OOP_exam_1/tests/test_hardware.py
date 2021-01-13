import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class HardwareTest(unittest.TestCase):

    def setUp(self):
        name = 'ssd'
        type = "ss"
        capacity = 600
        memory = 200
        self.hardware = Hardware(name, type, capacity, memory)

    def test_init(self):
        self.assertEqual(self.hardware.name, 'ssd')
        self.assertEqual(self.hardware.type, 'ss')
        self.assertEqual(self.hardware.capacity, 600)
        self.assertEqual(self.hardware.memory, 200)
        self.assertEqual(self.hardware.software_components, [])

    def test_install(self):
        software = ExpressSoftware('linux', 50, 15)
        expect_capacity = self.hardware.capacity - software.capacity_consumption
        expect_memory = self.hardware.memory - software.memory_consumption
        self.hardware.install(software)
        self.assertEqual(self.hardware.memory, expect_memory)
        self.assertEqual(self.hardware.capacity, expect_capacity)
        self.assertEqual(self.hardware.software_components[0], software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_install_2(self):
        software = ExpressSoftware('linux', 50, 350)
        expect = self.hardware.install(software)
        self.assertEqual('Software cannot be installed', expect)

    def test_uninstall(self):
        software = ExpressSoftware('linux', 50, 15)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(self.hardware.memory, 200)
        self.assertEqual(self.hardware.capacity, 600)
        self.assertEqual(self.hardware.software_components, [])

    def test_repr(self):
        actual = self.hardware
        self.assertEqual(print(actual), None)

    # def test_uninstall_2(self):
    #     software = ExpressSoftware('linux', 50, 15)
    #     self.assertEqual(self.hardware.uninstall(software), None)


if __name__ == '__main__':
    unittest.main()
