n = int(input())
the_list = []
the_max = []
for i in range(n):
    text_1, text_2 = input().split('-')
    tup_1 = tuple(text_1.split(','))
    tup_2 = tuple(text_2.split(','))
    max_ = max(int(tup_1[0]), int(tup_2[0]))
    min_ = min(int(tup_1[1]), int(tup_2[1]))
    intersection = []
    for j in range(max_, min_ + 1):
        intersection.append(j)
    the_list.append(intersection)
for el in the_list:
    if len(el) > len(the_max):
        the_max = el

print(f"Longest intersection is {the_max} with length {len(the_max)}")
