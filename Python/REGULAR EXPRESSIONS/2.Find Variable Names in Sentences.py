import re

names = input()
regex = r'\b_[a-zA-Z]*\b'
matches = re.findall(regex, names)
matches2 = [el[1:] for el in matches]
print(','.join(matches2))