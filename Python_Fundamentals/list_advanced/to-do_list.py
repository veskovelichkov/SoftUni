to_do_list = []
while True:
    command = input()
    if command == 'End':
        break
    command_split = command.split("-")
    index = int(command_split[0])
    task = command_split[1]
    to_do_list.append((index, task))
sorted_list = sorted(to_do_list)
new_list = [value[1] for value in sorted_list]
print(new_list)
