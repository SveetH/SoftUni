version = input().split(".")
version_2 = list(map(int, version))

for i in range(len(version_2) - 1, -1, -1):
    s = version_2[-1]
    if s == 9:
        version_2[-1] = 0
        version_2[-2] = version_2[-2] + 1
        if version_2[-2] == 10:
            version_2[-2] = 0
            version_2[-3] = version_2[-3] + 1

if int(version[-1]) == 9:
    print('.'.join(map(str, version_2)))
else:
    version_2[-1] += 1
    print('.'.join(map(str, version_2)))
