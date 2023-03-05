lines = int(input())
my_dict = {}
for _ in range(lines):
    line = input().split()
    command = line[0]
    name = line[1]
    if command == "register":
        plate = line[2]
        if name not in my_dict.keys():
            my_dict[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {my_dict[name]}")
    else:
        if name not in my_dict.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del my_dict[name]
for key, value in my_dict.items():
    print(f"{key} => {value}")
