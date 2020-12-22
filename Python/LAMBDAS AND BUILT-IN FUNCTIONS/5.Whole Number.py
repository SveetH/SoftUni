numbers = list(map(float, input().split(" ")))
print(sum([(round(el) * len(numbers)) for el in numbers]))
