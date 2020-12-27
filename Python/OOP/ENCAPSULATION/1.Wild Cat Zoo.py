class Lion:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Lion"

    def get_needs(self):
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Tiger"

    def get_needs(self):
        return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Cheetah"

    def get_needs(self):
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Keeper:

    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age
        self.type = "Keeper"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:

    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age
        self.type = "Caretaker"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:

    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age
        self.type = "Vet"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.type} added to the zoo"
        if len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.type} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        suma = sum([worker.salary for worker in self.workers])
        if suma <= self.__budget:
            self.__budget -= suma
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        suma = sum([a.get_needs() for a in self.animals])
        if suma <= self.__budget:
            self.__budget -= suma
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"
        result += f"----- {len([a for a in self.animals if a.type == 'Lion'])} Lions:\n"
        for a in [a for a in self.animals if a.type == 'Lion']:
            result += f"{repr(a)}\n"
        result += f"----- {len([a for a in self.animals if a.type == 'Tiger'])} Tigers:\n"
        for a in [a for a in self.animals if a.type == 'Tiger']:
            result += f"{repr(a)}\n"
        result += f"----- {len([a for a in self.animals if a.type == 'Cheetah'])} Cheetahs:\n"
        for a in [a for a in self.animals if a.type == 'Cheetah']:
            result += f"{repr(a)}\n"
        return result

    # def workers_status():
    #     return f"You have {total_workers_count} workers\n" \
    #            f"----- {amount_of_keepers} Keepers:\n" \
    #            f"{keeper1}\n" \
    #            f""


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
# print(zoo.workers_status())
