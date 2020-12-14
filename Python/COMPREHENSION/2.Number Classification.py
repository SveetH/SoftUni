words = [int(x) for x in input().split(", ")]
print(f'Positive: {", ".join([str(el) for el in words if el >= 0])}')
print(f'Negative: {", ".join([str(el) for el in words if el < 0])}')
print(f'Even: {", ".join(list(map(str, [el for el in words if el % 2 == 0])))}')
print(f'Odd: {", ".join(list(map(str, [el for el in words if el % 2 != 0])))}')
