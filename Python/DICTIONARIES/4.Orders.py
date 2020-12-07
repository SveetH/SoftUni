command = input()
all_ = []
products_price = {}
products_quantity = {}
while command != 'buy':
    all_ += command.split(' ')
    command = input()

for i in range(0, len(all_), 3):
    if all_[i] in products_quantity.keys():
        products_quantity[all_[i]] += float(all_[i + 2])
        continue
    key = all_[i]
    value = all_[i + 2]
    products_quantity[key] = float(value)

for s in range(0, len(all_), 3):
    key = all_[s]
    value = all_[s + 1]
    products_price[key] = float(value)

for key, value in products_price.items():
    bill = (products_price[key] * products_quantity[key])
    print(f'{key} -> {bill:.2f}')
