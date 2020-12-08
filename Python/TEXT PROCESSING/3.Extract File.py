strings = input().split('\\')
string = strings[-1].split('.')
print(F'File name: {string[0]}\nFile extension: {string[-1]}')
