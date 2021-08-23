command = input()
the_dict = dict()
while command != "search":
    name, number = command.split("-")
    the_dict[name] = number
    command = input()
command = input()
while command != "stop":
    if command in the_dict:
        print(f'{command} -> {the_dict[command]}')
    else:
        print(f"Contact {command} does not exist.")
    command = input()
