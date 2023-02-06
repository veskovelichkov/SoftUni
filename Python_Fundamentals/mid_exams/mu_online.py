dungeons_list = list(map(str, input().split("|")))
health = 100
bitcoins = 0
is_alive = True
best_room = 0
for fight in dungeons_list:
    battle = fight.split(" ")
    best_room += 1
    room = battle[0]
    value = int(battle[1])
    if room == 'potion':
        if value + health > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        else:
            print(f"You healed for {value} hp.")
            health += value
        print(f"Current health: {health} hp.")
    elif room == 'chest':
        print(f"You found {value} bitcoins.")
        bitcoins += value
    else:
        if health - value > 0:
            health -= value
            print(f"You slayed {room}.")
        else:
            print(f"You died! Killed by {room}.")
            print(f"Best room: {best_room}")
            is_alive = False
            break
if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
