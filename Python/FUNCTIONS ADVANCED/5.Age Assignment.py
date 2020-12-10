def age_assignment(*args, **kwargs):
    new_dict = dict()
    for el in args:
        for k, v in kwargs.items():
            if el[0] == k:
                new_dict[el] = v

    return new_dict


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))
