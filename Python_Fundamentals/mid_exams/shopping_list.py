product_cart = list(map(str, input().split('!')))
command = input()
while command != 'Go Shopping!':
    command_list = command.split(" ")
    if command_list[0] == 'Urgent':
        item = command_list[1]
        if item in product_cart:
            command = input()
            continue
        product_cart.insert(0, item)
    if command_list[0] == 'Unnecessary':
        item = command_list[1]
        if item not in product_cart:
            command = input()
            continue
        product_cart.remove(item)
    if command_list[0] == 'Correct':
        old_item = command_list[1]
        new_item = command_list[2]
        if old_item not in product_cart:
            command = input()
            continue
        product_cart = list(map(lambda x: x.replace(old_item, new_item), product_cart))
    if command_list[0] == 'Rearrange':
        item = command_list[1]
        if item not in product_cart:
            command = input()
            continue
        product_cart.remove(item)
        product_cart.append(item)
    command = input()
print(', '.join(product_cart))
