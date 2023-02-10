number_wagons = int(input())
list_wagons = [0] * number_wagons
while True:
    command = input()
    if command == "End":
        break
    command_split = command.split(" ")
    event = command_split[0]
    if event == "add":
        people = int(command_split[1])
        list_wagons[-1] += people
    elif event == "insert":
        index = int(command_split[1])
        people = int(command_split[2])
        list_wagons[index] += people
    elif event == "leave":
        index = int(command_split[1])
        people = int(command_split[2])
        list_wagons[index] -= people
print(list_wagons)
