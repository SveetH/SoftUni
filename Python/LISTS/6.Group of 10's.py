import math

numbers = input().split(", ")
numbers = list(map(int, numbers))
max_1 = math.ceil(max(numbers) / 10)
for i in range(1, max_1 + 1):
    filtered_numbers = list(filter((lambda x: 10 * (i - 1) < x < 10 * i + 1), numbers))
    print(f"Group of {i}0's: {filtered_numbers}")
