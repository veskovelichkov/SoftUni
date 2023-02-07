status_pirate_ship = list(map(int, input().split(">")))
status_warship = list(map(int, input().split(">")))
max_health_capacity = int(input())
command = input()
is_broken = False
while command != "Retire":
    command_split = command.split(" ")
    action = command_split[0]
    if action == "Fire":
        index = int(command_split[1])
        damage = int(command_split[2])
        if index < -200 or index > len(status_pirate_ship) or index > 200:
            command = input()
            continue
        status_warship[index] -= damage
        if status_warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            break
    elif action == "Defend":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        damage = int(command_split[3])
        if start_index < 0 or end_index >= len(status_pirate_ship):
            command = input()
            continue
        for i in range(start_index, end_index + 1):
            status_pirate_ship[i] -= damage
            if status_pirate_ship[i] <= 0:
                is_broken = True
                break
        if is_broken:
            print("You lost! The pirate ship has sunken.")
            break
    elif action == "Repair":
        index = int(command_split[1])
        health = int(command_split[2])
        if index < -200 or index > len(status_pirate_ship) or index > 200:
            command = input()
            continue
        if status_pirate_ship[index] + health > max_health_capacity:
            status_pirate_ship[index] = max_health_capacity
        else:
            status_pirate_ship[index] += health
    elif action == "Status":
        counter = 0
        for value in status_pirate_ship:
            if max_health_capacity * 0.2 > value:
                counter += 1
        print(f"{counter} sections need repair.")
    command = input()
if not is_broken:
    print(f"Pirate ship status: {sum(status_pirate_ship)}")
    print(f"Warship status: {sum(status_warship)}")
