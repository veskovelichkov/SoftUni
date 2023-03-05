my_dict = {}
while True:
    contact = input().split("-")
    if len(contact) == 1:
        break
    name = contact[0]
    number = contact[1]
    my_dict[name] = number
lines = int(contact[0])
for _ in range(lines):
    searched_name = input()
    if searched_name in my_dict.keys():
        print(f"{searched_name} -> {my_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
