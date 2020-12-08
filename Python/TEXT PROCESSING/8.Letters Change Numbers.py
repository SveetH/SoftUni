dic = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8',
       'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17',
       'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26',
       }

split_text = input().split()
final = 0
for el in split_text:
    letter_1 = el[0]
    letter_2 = el[-1]
    number = int(el[1:-1])
    if letter_1.isupper():
        number /= int(dic[letter_1.lower()])
    else:
        number *= int(dic[letter_1.lower()])
    if letter_2.isupper():
        number -= int(dic[letter_2.lower()])
    else:
        number += int(dic[letter_2.lower()])
    final += number

print(f"{final:.2f}")

