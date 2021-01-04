import re

text = input()
regex = r'(^|(?<=\s))[a-zA-Z0-9][a-zA-Z0-9_.+-]+[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
emails = re.finditer(regex, text)
emails_2 = [e.group() for e in emails]
for email in emails_2:
    if email[-1] == '.':
        email = email[:-1]
    print(email)
