words = input().split(', ')
dic = {el: len(el) for el in words}
li = []
for i, j in dic.items():
    li.append(f'{i} -> {j}')
print(', '.join(li))
