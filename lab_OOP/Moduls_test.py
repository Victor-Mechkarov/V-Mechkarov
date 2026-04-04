
store = {}

while True:
    command = input("Enter product: ")
    if command == "quit":
        break
    product_name = command
    values = []
    if product_name not in store:
       store[product_name] = values
       quantity = int(input("Enter quantity: "))
       values.append(quantity)
       price = float(input("Enter price: "))
       values.append(price)
    else:
        pass


for key, value in store.items():
    print(f"{key}: quantity: {value[0]} ; price: {value[1]}")



