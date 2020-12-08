string = input()
new_string = ""
for p in range(len(string)-1):
    if not string[p] == string[p+1]:
        new_string += string[p]
print(f'{new_string + string[-1]}')