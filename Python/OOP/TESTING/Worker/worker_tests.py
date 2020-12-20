import unittest

from worker import Worker


class WorkerTest(unittest.TestCase):

    def test_if_the_worker_is_initialized_with_correct_name_salary_and_energy(self):
        name = 'Ivan'
        salary = 250
        energy = 5
        worker = Worker(name, salary, energy)
        self.assertEqual(worker.name, name)
        self.assertEqual(worker.salary, salary)
        self.assertEqual(worker.salary, salary)
        self.assertEqual(worker.money, 0)

    def test_if_the_workers_energy_is_incremented_after_the_rest_method_is_called(self):
        name = 'Ivan'
        salary = 250
        energy = 6
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(worker.energy, energy + 1)

    def test_if_an_error_is_raised_when_the_worker_tries_to_work_with_negative_energy_or_equel_to_0(self):
        name = 'Ivan'
        salary = 250
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as cm:
            worker.work()
        self.assertIsNotNone(cm.exception)

    def test_if_the_workers_salary_increase_after_the_work_method_is_called(self):
        name = 'Ivan'
        salary = 250
        energy = 6
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.money, worker.salary)
        worker.work()
        self.assertEqual(worker.money, 2 * worker.salary)

    def test_if_the_workers_energy_is_decreased_after_the_work_method_is_called(self):
        name = 'Ivan'
        salary = 250
        energy = 6
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.energy, energy - 1)

    def test_if_the_get_info_method_returns_the_proper_string_with_correct_values(self):
        name = 'Ivan'
        salary = 250
        energy = 6
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.get_info(), f'{name} has saved {salary} money.')


if __name__ == '__main__':
    unittest.main()
