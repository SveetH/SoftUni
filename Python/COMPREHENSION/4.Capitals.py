enter_1 = input().split(', ')
enter_2 = input().split(', ')
zip_list = list(zip(enter_1, enter_2))
dict_countries = {el[0]: el[1] for el in zip_list}
[print(f"{k} -> {v}") for k, v in dict_countries.items()]