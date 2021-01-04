import re

names = input().lower()
regex = f'\\b{input()}\\b'
matches = re.findall(regex, names)
print(len(matches))