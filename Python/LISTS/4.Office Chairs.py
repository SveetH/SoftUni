rooms = int(input())
free = 0
not_enough = 0
for i in range(1, rooms + 1):
    s = input().split(" ")
    if len(s[0]) < int(s[1]):
        not_enough = int(s[1]) - len(s[0])
        print(F'{not_enough} more chairs needed in room {i}')
    else:
        free += len(s[0]) - int(s[1])
if not_enough == 0:
    print(F'Game On, {free} free chairs left')
