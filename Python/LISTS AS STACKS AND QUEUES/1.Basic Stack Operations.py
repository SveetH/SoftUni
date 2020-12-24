numbers = list(map(int, input().split()))
stack = list(map(int, input().split()))
n_app = numbers[0]
s_pop = numbers[1]
x = numbers[-1]

for i in range(s_pop):
    stack.pop()
if x in stack:
    print("True")
if not x in stack:
    print(min(stack))
if len(stack) == 0:
    print(0)
