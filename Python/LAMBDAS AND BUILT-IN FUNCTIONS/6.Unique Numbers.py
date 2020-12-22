numbers = [float(el) for el in input().split()]
round_numbers = [round(n) for n in numbers]
print(min(round_numbers))
print(max(round_numbers))


def multiply_unique(some_list):
    result = [3 * el for el in some_list]
    return set(result)


unique_numbers = sorted(list(multiply_unique(round_numbers)))
[print(el, end=" ") for el in unique_numbers]