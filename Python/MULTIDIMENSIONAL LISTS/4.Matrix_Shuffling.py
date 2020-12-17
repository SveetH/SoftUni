rows, cols = [int(x) for x in input().split(" ")]
matrix = []
for j in range(rows):
    line = [x for x in input().split(" ")]
    matrix.append(line)

commands = input()
while commands != "END":
    command = commands.split(" ")
    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
    else:
        first_index_1 = int(command[1])
        first_index_2 = int(command[2])
        second_index_1 = int(command[3])
        second_index_2 = int(command[4])
        try:
            matrix[first_index_1][first_index_2], matrix[second_index_1][second_index_2] = \
                matrix[second_index_1][second_index_2], matrix[first_index_1][first_index_2]
            [print(' '.join(x)) for x in matrix]
        except:
            print("Invalid input!")

    commands = input()
