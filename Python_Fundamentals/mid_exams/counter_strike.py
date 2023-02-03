initial_energy=int(input())
command=input()
won_battles=0
is_lost=False
counter=0
while command!='End of battle':
    distance=int(command)
    if initial_energy>=distance:
        won_battles+=1
        initial_energy-=distance
        counter+=1
        if counter==3:
            initial_energy+=won_battles
            counter=0
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        is_lost=True
        break
    command=input()
if not is_lost:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}" )