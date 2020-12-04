number = list(map(int, input().split(" ")))
input_string = input()
all_ = []
while input_string != "End":
    all_ = all_ + input_string.split(" ")
    input_string = input()
commands = all_[::3]
indexes = list(map(int, all_[1::3]))
values = list(map(int, all_[2::3]))
for i in range(len(commands)):
    if commands[i] == "Shoot":
        if 0 <= indexes[i] < len(number):
            number[indexes[i]] -= values[i]
            if number[indexes[i]] <= 0:
                del number[indexes[i]]
    if commands[i] == "Add":
        check = ""
        for j in range(0, len(number)):
            if indexes[i] == j:
                number.insert(indexes[i], values[i])
                check = "YES"
                break
            else:
                check = "NO"
        if check == "NO":
            print("Invalid placement!")
        if len(number) < 1:
            print("Invalid placement!")
    if commands[i] == "Strike":
        index = indexes[i]
        radius = values[i]
        if (index + radius) < len(number) and (index - radius) >= 0:
            number = number[:index - radius] + number[index + radius + 1:]
        else:
            print("Strike missed!")
number = list(map(str, number))
print('|'.join(number))
