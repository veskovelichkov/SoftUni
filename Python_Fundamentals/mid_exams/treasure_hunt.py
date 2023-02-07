initial_loot = list(map(str, input().split("|")))
command = input()
while command != "Yohoho!":
    command_split = command.split(" ")
    action = command_split[0]
    if action == "Loot":
        for i in range(1, len(command_split)):
            if command_split[i] not in initial_loot:
                initial_loot.insert(0, command_split[i])
    elif action == "Drop":
        index = int(command_split[1])
        if abs(index) >= len(initial_loot):
            command = input()
            continue
        initial_loot.append(initial_loot[index])
        initial_loot.pop(index)
    elif action == "Steal":
        count = int(command_split[1])
        if count >= len(initial_loot):
            print(", ".join(initial_loot))
            initial_loot = []
        else:
            stolen_items = initial_loot[len(initial_loot) - count:]
            print(", ".join(stolen_items))
            initial_loot = initial_loot[:len(initial_loot) - count]
    command = input()
sum_lenght = 0
for value in initial_loot:
    sum_lenght += len(value)
if sum_lenght > 0:
    print(f"Average treasure gain: {sum_lenght / len(initial_loot):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
