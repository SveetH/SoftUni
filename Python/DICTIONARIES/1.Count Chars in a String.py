word = input()
elements = {}
z = list(word)
for x in z:
    if x == " ":
        continue
    if x in elements.keys():
        elements[x] = elements[x] + 1
    else :
        elements[x] = 1
for k, v in elements.items():
    print('%s -> %d' % (k, v))