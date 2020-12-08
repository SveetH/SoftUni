string = input()
for p in range(len(string)):
    if string[p] == ':' and string[p + 1].isdigit() == False:
        print(string[p:p + 2])
