def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        takes = []
        num = 0
        for i in seq:
            takes.append(i)
            num += 1
            if num == n:
                break
        return takes

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# tests

# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# sum_first_n = sum(first_n(5))
# print(sum_first_n)
#
# for num in first_n(8):
#     print(num)
# def generator(maximum):
#     return (x for x in range(1, maximum + 1))
#
#
# s = generator(89)
# print((x for x in range(3)))
# print(f'\n')
# [print(el) for el in s]
