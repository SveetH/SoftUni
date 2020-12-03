command = input().lower().split(' ')
items_1 = {'shards': 0, 'fragments': 0, 'motes': 0}
items_2 = {}
check = ''
while True:
    for i in range(0, len(command), 2):
        if command[i + 1] in items_1.keys():
            items_1[command[i + 1]] += int(command[i])
            for key, value in items_1.items():
                if key == 'shards' and value >= 250:
                    check = 'Yes'
                    items_1[key] -= 250
                    print('Shadowmourne obtained!')
                    break
                if key == 'fragments' and value >= 250:
                    check = 'Yes'
                    items_1[key] -= 250
                    print('Valanyr obtained!')
                    break
                if key == 'motes' and value >= 250:
                    check = 'Yes'
                    items_1[key] -= 250
                    print('Dragonwrath obtained!')
                    break
            if check == 'Yes':
                break
            else:
                continue
        key = command[i + 1]
        value = command[i]
        items_1[key] = int(value)

    if check == 'Yes':
        break
    command = input().lower().split(' ')

items_2['motes'] = items_1['motes']
del items_1['motes']
items_2['shards'] = items_1['shards']
del items_1['shards']
items_2['fragments'] = items_1['fragments']
del items_1['fragments']

sorted_keys = sorted(items_1.keys(), key=lambda x: x.lower())
items_1_sort = {}
for key in sorted_keys:
    items_1_sort.update({key: items_1[key]})
items_2 = {k: v for k, v in sorted(items_2.items(), key=lambda item: (-item[1], item[0]))}

for key, value in items_2.items():
    print(f"{key}: {value}")
for key, value in items_1_sort.items():
    print(f"{key}: {value}")
