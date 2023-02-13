first_line = list(map(int, input().split(" ")))
second_line = list(map(int, input().split(" ")))
third_line = list(map(int, input().split(" ")))
first_player = False
second_player = False
if len(set(first_line)) == 1 or len((set(second_line))) == 1 or len((set(third_line))) == 1:
    if first_line[0] == 1:
        first_player = True
    elif first_line[0] == 2:
        second_player = True
if len((set(second_line))) == 1:
    if second_line[0] == 1:
        first_player = True
    elif second_line[0] == 2:
        second_player = True
if len((set(third_line))) == 1:
    if third_line[0] == 1:
        first_player = True
    elif third_line[0] == 2:
        second_player = True
for i in range(3):
    if first_line[i] == second_line[i] == third_line[i]:
        if first_line[0] == 1:
            first_player = True
        elif first_line[0] == 2:
            second_player = True
if first_line[0] == second_line[1] == third_line[2]:
    if first_line[0] == 1:
        first_player = True
    elif first_line[0] == 2:
        second_player = True
if first_line[2] == second_line[1] == third_line[0]:
    if first_line[2] == 1:
        first_player = True
    elif first_line[2] == 2:
        second_player = True
if first_player:
    print("First player won")
elif second_player:
    print("Second player won")
elif not first_player and not second_player:
    print("Draw!")
