rows, cols = [int(x) for x in input().split(" ")]
matrix = []
for j in range(rows):
    line = [int(x) for x in input().split(" ")]
    matrix.append(line)
max_sum = 0
max_a = 0
max_b = 0
max_c = 0
for row in range(0, rows - 2):
    for col in range(0, cols - 2):
        a = matrix[row][col:col + 3]
        b = matrix[row + 1][col:col + 3]
        c = matrix[row + 2][col:col + 3]
        total_sum = sum(a) + sum(b) + sum(c)
        if total_sum > max_sum:
            max_sum = total_sum
            max_a = a
            max_b = b
            max_c = c

print(f"Sum = {max_sum}")
print(' '.join(map(str, max_a)))
print(' '.join(map(str, max_b)))
print(' '.join(map(str, max_c)))
