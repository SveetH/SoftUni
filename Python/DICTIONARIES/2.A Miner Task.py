command = input().lower().split(' ')
items_1 = {}
items_2 = {}
check = ''
while True:
    for i in range(0, len(command), 2):
        if command[i + 1] in items_1.keys():
            items_1[command[i + 1]] += int(command[i])
            continue
        key = command[i + 1]
        value = command[i]
        items_1[key] = int(value)
        if key == 'shards' and items_1[key] >= 250:
            check = 'Yes'
            items_1[key] -= 250
            print('Shadowmourne obtained!')
            break
        if key == 'fragments' and items_1[key] >= 250:
            check = 'Yes'
            items_1[key] -= 250
            print('Dragonwrath obtained!')
            break
        if key == 'motes' and items_1[key] >= 250:
            check = 'Yes'
            items_1[key] -= 250
            print('Valanyr obtained!')
            break
    if check == 'Yes':
        break
    command = input().lower().split(' ')

items_2['motes'] = items_1['motes']
del items_1['motes']
items_2['shards'] = items_1['shards']
del items_1['shards']
items_2['fragments'] = items_1['fragments']
del items_1['fragments']

items_s = dict(sorted(items_1.items(), key=lambda kv: kv[1], reverse=True))
items_2 = {k: v for k, v in sorted(items_2.items(), key=lambda item: item[1], reverse=True)}

for key, value in items_2.items():
    print(f"{key}: {value}")
for key, value in items_s.items():
    print(f"{key}: {value}")
