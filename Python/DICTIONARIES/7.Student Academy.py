number_students = int(input())
all_ = list()
dic = {}
for j in range(number_students * 2):
    all_.append(input())
students = all_[0:-1:2]
grades = all_[1::2]
for s in range(len(students)):
    if not students[s] in dic:
        dic[students[s]] = float(grades[s])
    else:
        dic[students[s]] += float(grades[s])
        value = dic[students[s]]
        dic[students[s]] = value / 2

dic = dict(sorted(dic.items(), key=lambda x: float(x[1]), reverse=True))
[print(f"{k} -> {v:.2f}") for k, v in dic.items() if v >= 4.50]
