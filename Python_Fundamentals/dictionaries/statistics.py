command = input()
bakery = {}
while True:
    if command == "statistics":
        break
    command_split = command.split(": ")
    product = command_split[0]
    quantity = int(command_split[1])
    if product not in bakery.keys():
        bakery[product] = 0
    bakery[product] += quantity
    command = input()
print("Products in stock:")
for key in bakery.keys():
    print(f"- {key}: {bakery[key]}")
print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")
