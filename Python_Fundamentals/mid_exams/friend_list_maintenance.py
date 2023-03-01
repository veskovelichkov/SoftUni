def blacklist(friend, name):
    if name in friend:
        name_index = friend.index(name)
        friend[name_index] = "Blacklisted"
        print(f"{name} was blacklisted.")
    else:
        print(f"{name} was not found.")
    return friend


def error(friend, index):
    if index in range(len(friend)):
        friend_name = friend[index]
        if friend_name != "Blacklisted" and friend_name != "Lost":
            print(f"{friend[index]} was lost due to an error.")
            friend[index] = "Lost"
    return friend


def change(friend, index, name):
    if index in range(len(friend)):
        print(f"{friend[index]} changed his username to {name}.")
        friend[index] = name
    return friend


friends = input().split(", ")
command = input()
while True:
    if command == "Report":
        break
    command_split = command.split(" ")
    event = command_split[0]
    name_or_index = command_split[1]
    if event == "Blacklist":
        friends = blacklist(friends, name_or_index)
    elif event == "Error":
        name_or_index = int(name_or_index)
        friends = error(friends, name_or_index)
    elif event == "Change":
        name_or_index = int(name_or_index)
        new_name = command_split[2]
        friends = change(friends, name_or_index, new_name)
    command = input()
print(f"Blacklisted names: {friends.count('Blacklisted')}")
print(f"Lost names: {friends.count('Lost')}")
print(' '.join(friends))
