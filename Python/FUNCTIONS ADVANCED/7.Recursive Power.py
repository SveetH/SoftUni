def recursive_power(power, limit):
    if limit == 1:
        return power
    return power * recursive_power(power, limit - 1)


print((recursive_power(2, 10)))
# print(recursive_power(10, 100))
