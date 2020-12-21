rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

active_cells = []
sum_of_active = 0
commands = input().split(" ")
for i in range(len(commands)):
    c_row = int(commands[i][0])
    c_col = int(commands[i][2])
    damage = matrix[c_row][c_col]
    matrix[c_row][c_col] = "0"

    try:
        if c_row >= 1 and c_col >= 1:
            matrix[c_row - 1][c_col - 1] -= damage
            if matrix[c_row - 1][c_col - 1] <= 0:
                matrix[c_row - 1][c_col - 1] = str(matrix[c_row - 1][c_col - 1])

    except:
        pass

    try:

        if c_row >= 1:
            matrix[c_row - 1][c_col] -= damage
            if matrix[c_row - 1][c_col] <= 0:
                matrix[c_row - 1][c_col] = str(matrix[c_row - 1][c_col])

    except:
        pass

    try:

        if c_row >= 1:
            matrix[c_row - 1][c_col + 1] -= damage
            if matrix[c_row - 1][c_col + 1] <= 0:
                matrix[c_row - 1][c_col + 1] = str(matrix[c_row - 1][c_col + 1])

    except:
        pass

    try:

        if c_col >= 1:
            matrix[c_row][c_col - 1] -= damage
            if matrix[c_row][c_col - 1] <= 0:
                matrix[c_row][c_col - 1] = str(matrix[c_row][c_col - 1])

    except:
        pass

    try:

        matrix[c_row][c_col + 1] -= damage
        if matrix[c_row][c_col + 1] <= 0:
            matrix[c_row][c_col + 1] = str(matrix[c_row][c_col + 1])

    except:
        pass

    try:

        if c_col >= 1:
            matrix[c_row + 1][c_col - 1] -= damage
            if matrix[c_row + 1][c_col - 1] <= 0:
                matrix[c_row + 1][c_col - 1] = str(matrix[c_row + 1][c_col - 1])

    except:
        pass

    try:

        matrix[c_row + 1][c_col] -= damage
        if matrix[c_row + 1][c_col] <= 0:
            matrix[c_row + 1][c_col] = str(matrix[c_row + 1][c_col])

    except:
        pass

    try:

        matrix[c_row + 1][c_col + 1] -= damage
        if matrix[c_row + 1][c_col + 1] <= 0:
            matrix[c_row + 1][c_col + 1] = str(matrix[c_row + 1][c_col + 1])
    except:
        pass

for l in matrix:
    sum_of_active += sum([x for x in l if type(x) == int])
    active_cells += [x for x in l if type(x) == int]
print(f"Alive cells: {len(active_cells)}")
print(f"Sum: {sum_of_active}")
[print(' '.join(map(str, x))) for x in matrix]
