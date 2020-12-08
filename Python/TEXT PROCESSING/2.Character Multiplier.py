strings = input().split(" ")
length = min(len(strings[0]), len(strings[1]))
sum_1 = 0
for a, b in zip(strings[0], strings[1]):
    sum_1 += ord(a) * ord(b)
if len(strings[0]) > len(strings[1]):
    word = strings[0][length:]
    for i in word:
        sum_1 += ord(word)
elif len(strings[0]) < len(strings[1]):
    for i in range(len(strings[1]) - length):
        sum_1 += ord(strings[1][length + i])

print(sum_1)
