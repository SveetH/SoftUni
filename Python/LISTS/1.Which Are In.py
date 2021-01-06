s1 = input().split(", ")
s2 = input().split(", ")
s3 = []
s4 = []
for i in range(len(s1)):
    s3 = [x for x in s2 if str(s1[i]) in x]
    for j in range(len(s3)):
        f = str(s1[i])
        s4.append(f)
s4 = list(dict.fromkeys(s4))
print(s4)
