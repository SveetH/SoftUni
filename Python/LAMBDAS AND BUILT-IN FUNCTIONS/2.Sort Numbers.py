command = input().split(" ")
init_l = len(command)


def get_int(ll):
    check = ""
    int_list = list()
    for el in ll:
        for x in el:
            if 48 <= ord(x) <= 57:
                check = 'Y'
            else:
                check = 'N'
                break
        if check == 'Y':
            int_list.append(el)
    return sorted(map(int, int_list))


result = list(filter(lambda i: i > init_l, get_int(command)))
[print(el, end=' ') for el in result]
