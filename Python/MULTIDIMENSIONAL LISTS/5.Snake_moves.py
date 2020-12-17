rows, cols = [int(x) for x in input().split(" ")]
matrix = []
for j in range(rows):
    matrix.append("")

string = input()
for i in range(rows):
    if i % 2 == 0:
        for j in range(cols):
            element = string[0]
            string = string[1:]
            matrix[i] += element
            string += element
    else:
        for s in range(cols):
            element = string[0]
            string = string[1:]
            matrix[i] += element
            string += element
        ll = matrix[i]
        matrix[i] = ll[::-1]

[print(x) for x in matrix]
