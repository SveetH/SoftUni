secret_message = input().split(" ")


def decipher(value):
    c = ""
    b = ""
    for i in value:
        if i.isdigit():
            c += i
        else:
            b += i
    return chr(int(c)) + b


for j in range(0, len(secret_message)):
    word = secret_message[j]
    d_word = decipher(word)
    t = list(d_word)
    t[1], t[-1] = t[-1], t[1]
    print(''.join(t), end=" ")
