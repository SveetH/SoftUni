number = int(input())
command = list(map(int, input().split(" ")))
multiply_list = list(map(lambda x: x * number, command))
[print(el, end=" ") for el in multiply_list]
