

warehouse = {}
while True:
    command = input()
    if command == "end":
        break
    product = command
    amount = int(input())
    if product not in warehouse.keys():
        warehouse[product] = amount

    else:
        warehouse[product] += amount

for key, value in warehouse.items():
    print(f"{key}: {value}")
