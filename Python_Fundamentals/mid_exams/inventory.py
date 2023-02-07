inventory_journal = list(map(str, input().split(", ")))
command = input()
while command != "Craft!":
    command_split = command.split(" - ")
    event = command_split[0]
    item = command_split[1]
    if event == "Collect":
        if item not in inventory_journal:
            inventory_journal.append(item)
    elif event == "Drop":
        if item in inventory_journal:
            inventory_journal.remove(item)
    elif event == "Combine Items":
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory_journal:
            index_old_item=inventory_journal.index(old_item)
            inventory_journal.insert(index_old_item+1,new_item)
    elif event == "Renew":
        if item in inventory_journal:
            inventory_journal.remove(item)
            inventory_journal.append(item)
    command = input()
print(", ".join(inventory_journal))
