my_dict = {}
order = input()
while True:
    if order == "buy":
        break
    order_split = order.split(" ")
    product, price, quantity = order_split[0], float(order_split[1]), int(order_split[2])
    if product not in my_dict.keys():
        my_dict[product] = [price, quantity]
    else:
        my_dict[product][0] = price
        my_dict[product][1] += quantity
    order = input()
for key, value in my_dict.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")
