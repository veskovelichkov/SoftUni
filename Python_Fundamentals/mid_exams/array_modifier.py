sequence = list(map(int, input().split(" ")))
command = input()
while command != 'end':
    command_list = command.split(" ")
    if len(command_list) == 1:
        for i in range(0, len(sequence)):
            sequence[i] = sequence[i] - 1
    elif len(command_list) == 3:
        comm = command_list[0]
        index1 = int(command_list[1])
        index2 = int(command_list[2])
        if comm == 'swap':
            sequence[index1], sequence[index2] = sequence[index2], sequence[index1]
        elif comm == 'multiply':
            sequence[index1] = sequence[index2] * sequence[index1]
    command = input()
sequence = map(str, sequence)
print(', '.join(sequence))
