n = int(input())
the_list = []
new_list = []
for char in range(0, n):
    the_list.append(input().split(" "))
for el in the_list:
    for pos in el:
        new_list.append(pos)
new_list = list(set(new_list))
for ch in new_list:
    print(ch)
