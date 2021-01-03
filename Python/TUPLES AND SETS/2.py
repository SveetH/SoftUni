inp = [int(el) for el in input().split(" ")]
first = []
second = []
for i in range(0, inp[0]):
    first.append(input())
for j in range(0, inp[-1]):
    second.append(input())
sums = [char for char in first if char in second]
sums = list(set(sums))
for el in sums:
    print(el)
