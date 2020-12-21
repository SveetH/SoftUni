rows = int(input())
cols = rows
matrix = []
commands = input().split(" ")
for i in range(rows):
    matrix.append([x for x in input().split(" ")])
count = 0
c_count = 0
c_r = 0
c_c = 0
check = ""
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "s":
            c_r = i
            c_c = j

for s in range(rows):
    for l in range(cols):
        if matrix[s][l] == "c":
            c_count += 1
for el in commands:
    if el == "up":
        if c_r >= 1:
            if matrix[c_r - 1][c_c] == "e":
                print(f"Game over! ({c_r - 1}, {c_c})")
                check = "Y"
                break
            try:
                if matrix[c_r - 1][c_c] == "c":
                    count += 1
                    matrix[c_r - 1][c_c] = "s"
                    matrix[c_r][c_c] = "*"
                    c_r -= 1
                else:
                    matrix[c_r - 1][c_c] = "s"
                    matrix[c_r][c_c] = "*"
                    c_r -= 1
            except:
                pass
    if el == "down":
        if c_r < rows - 1:
            if matrix[c_r + 1][c_c] == "e":
                print(f"Game over! ({c_r + 1}, {c_c})")
                check = "Y"
                break
            try:
                if matrix[c_r + 1][c_c] == "c":
                    count += 1
                    matrix[c_r + 1][c_c] = "s"
                    matrix[c_r][c_c] = "*"
                    c_r += 1
                else:
                    matrix[c_r + 1][c_c] = "s"
                    matrix[c_r][c_c] = "*"
                    c_r += 1
            except:
                pass
    if el == "left":
        if c_c >= 1:
            if matrix[c_r][c_c - 1] == "e":
                print(f"Game over! ({c_r}, {c_c - 1})")
                check = "Y"
                break
            try:
                if matrix[c_r][c_c - 1] == "c":
                    count += 1
                    matrix[c_r][c_c - 1] = "s"
                    matrix[c_r][c_c] = "*"
                    c_c -= 1
                else:
                    matrix[c_r][c_c - 1] = "s"
                    matrix[c_r][c_c] = "*"
                    c_c -= 1
            except:
                pass
    if el == "right":
        if c_c < rows - 1:
            if matrix[c_r][c_c + 1] == "e":
                print(f"Game over! ({c_r}, {c_c + 1})")
                check = "Y"
                break
            try:
                if matrix[c_r][c_c + 1] == "c":
                    count += 1
                    matrix[c_r][c_c + 1] = "s"
                    matrix[c_r][c_c] = "*"
                    c_c += 1
                else:
                    matrix[c_r][c_c + 1] = "s"
                    matrix[c_r][c_c] = "*"
                    c_c += 1
            except:
                pass
f_r = 0
f_c = 0
for k in range(rows):
    for x in range(cols):
        if matrix[k][x] == "s":
            f_r = k
            f_c = x

if check != "Y":
    if count == c_count:
        print(f"You collected all coals! ({f_r}, {f_c})")
    else:
        print(f"{c_count - count} coals left. ({f_r}, {f_c})")
