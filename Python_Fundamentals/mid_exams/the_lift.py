people_waiting = int(input())
current_state_of_lift = list(map(int, input().split(" ")))
new_state_of_lift = []
for value in current_state_of_lift:
    if value == 4:
        new_state_of_lift.append(4)
        continue
    if people_waiting - (4 - value) >= 0:
        new_state_of_lift.append(4)
        people_waiting -= (4 - value)
    else:
        if people_waiting + value <= 4:
            new_state_of_lift.append(people_waiting + value)
            people_waiting = 0
        else:
            new_state_of_lift.append(4)
            people_waiting -= (4 - value)
new_state_of_lift = list(map(str, new_state_of_lift))
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(' '.join(new_state_of_lift))
else:
    if all(wagons == '4' for wagons in new_state_of_lift):
        print(' '.join(new_state_of_lift))
    else:
        print("The lift has empty spots!")
        print(' '.join(new_state_of_lift))
