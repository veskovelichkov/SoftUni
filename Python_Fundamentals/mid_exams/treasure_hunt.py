loot_list = list(map(str, input().split("|")))
command = input()
while command != "Yohoho!":
    command_list = command.split(" ")
    event = command_list[0]
    if event == 'Loot':
        for index in range(1, len(command_list)):
            if command_list[index] not in loot_list:
                loot_list.insert(0, command_list[index])
    elif event == 'Drop':
        index = int(command_list[1])
        if index >= len(loot_list):
            continue
        else:
            loot_list.append(loot_list[index])
            loot_list.pop(index)
    elif event=='Steal':
        count=int(command_list[1])
        if count>len(loot_list):
            print(', '.join(loot_list))
            loot_list=[]
        else:
            print(', '.join(loot_list[count-1:]))
            loot_list=loot_list[:-count]
    command = input()
