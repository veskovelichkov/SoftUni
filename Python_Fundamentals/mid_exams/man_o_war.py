def fire_ship(current_warship_status, current_index, current_damage):
    is_broken = False
    if current_index in range(len(current_warship_status)):
        current_warship_status[current_index] -= current_damage
        if current_warship_status[current_index] <= 0:
            is_broken = True
    return current_warship_status, is_broken


def defend_ship(current_pirate_ship_status, first_index, second_index, current_damage):
    is_broken = False
    if first_index in range(len(current_pirate_ship_status)) and second_index in range(len(current_pirate_ship_status)):
        for i in range(first_index, second_index + 1):
            current_pirate_ship_status[i] -= current_damage
            if current_pirate_ship_status[i] <= 0:
                is_broken = True
    return current_pirate_ship_status, is_broken


def current_status(current_pirate_ship_status, maximum_health):
    counter = 0
    for value in current_pirate_ship_status:
        if value < 0.2 * maximum_health:
            counter += 1
    return counter


def repair_ship(current_pirate_ship_status, chosen_index, chosen_health, maximum_health):
    if chosen_index in range(len(current_pirate_ship_status)):
        current_pirate_ship_status[chosen_index] += chosen_health
        if current_pirate_ship_status[chosen_index] > maximum_health:
            current_pirate_ship_status[chosen_index] = maximum_health
    return current_pirate_ship_status


pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health = int(input())
while True:
    command = input()
    is_won = False
    is_lost = False
    if command == "Retire":
        break
    command_split = command.split(" ")
    event = command_split[0]
    if command == "Status":
        repairs_needed = current_status(pirate_ship_status, max_health)
        print(f"{repairs_needed} sections need repair.")
    elif event == "Fire":
        index = int(command_split[1])
        damage = int(command_split[2])
        warship_status, is_won = fire_ship(warship_status, index, damage)
        if is_won:
            print("You won! The enemy ship has sunken.")
            break
    elif event == "Defend":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        damage = int(command_split[3])
        pirate_ship_status, is_lost = defend_ship(pirate_ship_status, start_index, end_index, damage)
        if is_lost:
            print("You lost! The pirate ship has sunken.")
            break
    elif event == "Repair":
        index = int(command_split[1])
        health = int(command_split[2])
        pirate_ship_status = repair_ship(pirate_ship_status, index, health, max_health)
if not is_lost and not is_won:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
