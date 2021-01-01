# Version 1

a = [int(el) for el in input().split(" ")]


def fractionalized(i):
    divisor = 9
    while divisor < i:
        divisor = 10 * divisor + 9

    return i / divisor


a = sorted(a, key=fractionalized, reverse=True)
print(''.join(map(str, a)))

# Version 2

# numbers = input().split(' ')
# numbers.sort(key=max)
# numbers.reverse()
# print(''.join(numbers))
