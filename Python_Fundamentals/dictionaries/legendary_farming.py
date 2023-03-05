my_dict = {"shards": 0, "fragments": 0, "motes": 0}
is_obtained = False
while not is_obtained:
    recipe = input().lower().split(" ")
    for index in range(0, len(recipe), 2):
        if recipe[index + 1] not in my_dict:
            my_dict[recipe[index + 1]] = 0
        my_dict[recipe[index + 1]] += int(recipe[index])
        if my_dict["shards"] >= 250:
            my_dict["shards"] -= 250
            print("Shadowmourne obtained!")
            is_obtained = True
        elif my_dict["fragments"] >= 250:
            my_dict["fragments"] -= 250
            print("Valanyr obtained!")
            is_obtained = True
        elif my_dict["motes"] >= 250:
            my_dict["motes"] -= 250
            print("Dragonwrath obtained!")
            is_obtained = True
        if is_obtained:
            break
    if is_obtained:
        break
for key, value in my_dict.items():
    print(f"{key}: {value}")
