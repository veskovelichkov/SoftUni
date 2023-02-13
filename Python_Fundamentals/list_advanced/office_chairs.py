def free_spaces(rooms):
    total_free_chairs = 0
    full_room = False
    for single_room in range(1, rooms+1):
        layout = input().split(" ")
        chairs = len(layout[0])
        participants = int(layout[1])
        if chairs < participants:
            print(f"{participants - chairs} more chairs needed in room {single_room}")
            full_room = True
        else:
            total_free_chairs += chairs - participants
    return total_free_chairs, full_room


number_of_rooms = int(input())
free_chairs, is_full = free_spaces(number_of_rooms)
if not is_full:
    print(f"Game On, {free_chairs} free chairs left")