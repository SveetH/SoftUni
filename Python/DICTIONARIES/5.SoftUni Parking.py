n = int(input())
register = dict()
for i in range(n):
    input_all = input().split(" ")
    if input_all[0] == "register":
        if not input_all[1] in register.keys():
            register[input_all[1]] = input_all[2]
            print(f"{input_all[1]} registered {input_all[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {input_all[2]}")
    if input_all[0] == "unregister":
        if not input_all[1] in register.keys():
            print(f"ERROR: user {input_all[1]} not found")
        else:
            register.pop(input_all[1])
            print(f"{input_all[1]} unregistered successfully")

[print(f"{k} => {v}") for k, v in register.items()]