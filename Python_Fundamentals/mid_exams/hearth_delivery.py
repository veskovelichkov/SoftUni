neighborhood = list(map(int, input().split("@")))
position = 0
command = input()
while command != 'Love!':
    command_split = command.split()
    jump = int(command_split[1])
    position += jump
    if position >= len(neighborhood):
        position = 0
    neighborhood[position] -= 2
    if neighborhood[position] < 0:
        print(f"Place {position} already had Valentine's day.")
    elif neighborhood[position] == 0:
        print(f"Place {position} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {position}.")
if all([value <= 0 for value in neighborhood]):
    print("Mission was successful.")
else:
    places_failed = [value for value in neighborhood if value > 0]
    print(f"Cupid has failed {len(places_failed)} places.")
