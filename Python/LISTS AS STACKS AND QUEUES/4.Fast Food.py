from collections import deque

food_quantity = int(input())
list_ = list(map(int, input().split()))
queue = deque(list_)
max_order = max(list_)
for el in list_:
    if food_quantity >= el:
        food_quantity -= el
        queue.popleft()
if not len(queue) == 0:
    print(max_order)
    print(f"Orders left: {' '.join(map(str, queue))}")
else:
    print(max_order)
    print(f"Orders complete")
