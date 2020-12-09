text = input().split('@')
text = list(map(int, text))
command = input()
s = 0
check = ""
while command != 'Love!':
    jump = command.split(' ')
    x = int(jump[-1])
    s += x
    if s > (len(text) - 1):
        s = 0
    text[s] -= 2
    if -20 < text[s] <= 0:
        print(f"Place {s} has Valentine's day.")
        text[s] = -30
    elif text[s] < -21:
        print(f"Place {s} already had Valentine's day.")

    command = input()

print(f'Cupid\'s last position was {s}.')
for i in text:
    if i > 0:
        print(f"Cupid has failed {len([n for n in text if n > 0])} places.")
        check = "yes"
        break
if not check == "yes":
    print("Mission was successful.")
