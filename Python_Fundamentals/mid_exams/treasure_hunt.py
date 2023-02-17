def drop_item(treasury, current_index):
    if current_index in range(len(treasury)):
        removed_item = treasury.pop(current_index)
        treasury.append(removed_item)
    return treasury


def steal_items(treasury, counter):
    if counter > len(treasury):
        print(", ".join(treasury))
        treasury = []
    else:
        print(", ".join(treasury[len(treasury) - counter:]))
        treasury = treasury[0:len(treasury) - counter]
    return treasury


def loot_items(treasury, looted_items):
    for value in looted_items:
        if value not in treasury:
            treasury.insert(0, value)
    return treasury


treasure = input().split("|")
while True:
    command = input()
    if command == "Yohoho!":
        break
    command_split = command.split(" ")
    event = command_split[0]
    if event == "Loot":
        items = command_split[1:]
        treasure = loot_items(treasure, items)
    elif event == "Drop":
        index = int(command_split[1])
        treasure = drop_item(treasure, index)
    elif event == "Steal":
        count = int(command_split[1])
        treasure = steal_items(treasure, count)
if treasure==[]:
    print("Failed treasure hunt.")
else:
    sum_len=sum([len(value) for value in treasure])
    print(f"Average treasure gain: {sum_len/len(treasure):.2f} pirate credits.")
