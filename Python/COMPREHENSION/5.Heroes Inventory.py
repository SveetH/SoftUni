names = input().split(", ")
dicts = [dict() for x in names]
command = input()

while command != "End":
    command = command.split("-")
    name = command[0]
    item = command[1]
    price = command[2]
    for i in range(len(names)):
        if name == names[i]:
            if item not in dicts[i]:
                dicts[i][item] = price
    command = input()

for j in range(len(names)):
    sum_j = sum([int(v) for v in dicts[j].values()])
    print(f"{names[j]} -> Items: {len(dicts[j])}, Cost: {sum_j}")
