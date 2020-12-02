n = int(input())
sum_1 = 0
count = 0
s = []
while sum_1 <= n:
    count += 1
    c_power = 2 * (pow(count, 2))
    sum_1 += c_power
    if sum_1 > n:
        s = list(map(int, s))
        s.append(n - sum(s))
        break

    s.append(str(c_power))
if s[-1] == 0:
    s.pop()
print(s)
