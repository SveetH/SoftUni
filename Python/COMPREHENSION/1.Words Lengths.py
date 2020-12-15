words = input().split(', ')
dic = {el: len(el) for el in words}
print(*[f'{i} -> {j}' for i, j in dic.items()], sep=', ')
