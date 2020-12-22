numbers = list(map(int, input().split(" ")))
negative = list(filter(lambda el: el < 0, numbers))
print(abs(sum(negative)))