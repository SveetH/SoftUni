rows, cols = [int(x) for x in input().split(" ")]
matrix = []

for j in range(rows):
    line = [x for x in input().split(" ")]
    matrix.append(line)

count = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        current = matrix[row][col]
        r = matrix[row][col + 1]
        d = matrix[row + 1][col]
        dr = matrix[row + 1][col + 1]
        if current == r == d == dr:
            count += 1

print(f"{count}")
