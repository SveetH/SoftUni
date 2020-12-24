n = int(input())
stack = []
for i in range(0, n):
    command = input().split(' ')
    command = list(map(int, command))
    if command[0] == 1:
        stack.append(command[-1])
    elif command[0] == 2 and len(stack) > 0:
        stack.pop()
    elif command[0] == 3 and len(stack) > 0:
        print(max(stack))
    elif command[0] == 4 and len(stack) > 0:
        print(min(stack))
stack = reversed(list(map(str, stack)))
print(', '.join(stack))
