def func_executor(*tuples):
    new_list = []
    for tup in tuples:
        el = tup[0](*tup[1])
        new_list.append(el)
    return new_list


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
# expected result = [3, 8]
