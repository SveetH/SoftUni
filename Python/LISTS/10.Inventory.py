items = input().split(", ")
command = input()
all_ = []
s = 0
while command != "Craft!":
    all_ += command.split(" - ")
    command = input()
commands = all_[0::2]
items_1 = all_[1::2]
for i in range(len(commands)):
    if commands[i] == "Collect":
        items.append(items_1[i])
    if commands[i] == "Drop":
        for j in range(len(items)):
            if items[j] == items_1[i]:
                del items[j]
                break
    if commands[i] == "Combine Items":
        combine = items_1[i].split(":")
        for s in range(len(items)):
            if items[s] == combine[0]:
                items.insert(s + 1, combine[1])
    if commands[i] == "Renew":
        for l in range(len(items)):
            if items[l] == items_1[i]:
                items.remove(items_1[i])
                items.append(items_1[i])

items = list(dict.fromkeys(items))
print(', '.join(items))
