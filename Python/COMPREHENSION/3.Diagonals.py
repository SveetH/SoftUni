n = int(input())
matrix = [[int(el) for el in input().split(', ')] for i in range(0, n)]
first = []
second = []
index = 0
index2 = -1
for el in matrix:
    second.append(el[index2])
    first.append(el[index])
    index += 1
    index2 -= 1

print(f"First diagonal: {', '.join([str(el) for el in first])}. Sum: {sum(first)}")
print(f"Second diagonal: {', '.join([str(el) for el in second])}. Sum: {sum(second)}")
