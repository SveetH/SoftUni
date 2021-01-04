import re

pattern = r"www.[a-zA-Z0-9-]+\.[a-z.]+"
command = input()
while command:
    result = re.findall(pattern, command)
    if len(result) > 0:
        [print(el) for el in result]

    command = input()
