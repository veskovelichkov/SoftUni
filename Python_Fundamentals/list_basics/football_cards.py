string=input()
my_list=string.split(" ")
players_A=11
players_B=11
no_duplicates=[]
[no_duplicates.append(value) for value in my_list if value not in no_duplicates]
for player in no_duplicates:
    if player[0]=="A":
        players_A-=1
    else:
        players_B-=1
    if players_A < 7 or players_B < 7:
        break
print(f"Team A - {players_A}; Team B - {players_B}")
if players_A<7 or players_B<7:
    print("Game was terminated")