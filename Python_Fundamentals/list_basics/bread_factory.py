events=input().split('|')
energy=100
coins=100
is_opened=True
for event in events:
    event_items=event.split('-')
    type_of_event=event_items[0]
    event_value=int(event_items[1])
    if type_of_event=='rest':
        current_energy=energy
        energy+=event_value
        if energy>100:
            energy=100
        gained_energy=energy-current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif type_of_event=="order":
        if energy>=30:
            energy-=30
            coins+=event_value
            print(f"You earned {event_value} coins.")
        else:
            energy+=50
            print("You had to rest!")
    else:
        if coins>=event_value:
            print(f'You bought {type_of_event}.')
            coins-=event_value
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            is_opened=False
            break
if is_opened:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")