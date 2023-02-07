sequence_targets = list(map(int, input().split(" ")))
command = input()
while command != 'End':
    command_list = command.split(" ")
    action = command_list[0]
    if action == "Shoot":
        index = int(command_list[1])
        power = int(command_list[2])
        if index < 0 or index >= len(sequence_targets):
            print("Invalid placement!")
            command = input()
            continue
        sequence_targets[index] -= power
        if sequence_targets[index] <= 0:
            sequence_targets.pop(index)
    elif action == "Add":
        index = int(command_list[1])
        value = int(command_list[2])
        if index < 0 or index > len(sequence_targets):
            print("Invalid placement!")
            command = input()
            continue
    if action == "Strike":
        index = int(command_list[1])
        radius = int(command_list[2])
        if index < 0 or index >= len(sequence_targets):
            print("Strike missed!")
            command = input()
            continue
        elif index - radius < 0 or index + radius >= len(sequence_targets):
            print("Strike missed!")
            command = input()
            continue
        else:
            sequence_targets = sequence_targets[:index - radius] + sequence_targets[index + radius + 1:]
    command = input()
sequence_targets=list(map(str,sequence_targets))
print("|".join(sequence_targets))
