sequence_list = list(map(str, input().split(" ")))
command = input()
moves = 0
is_solved = False
while command != "end":
    moves += 1
    index_list = command.split(" ")
    first_index = int(index_list[0])
    second_index = int(index_list[1])
    if first_index < 0 or second_index < 0 or first_index >= len(sequence_list) or second_index >= len(
            sequence_list) or first_index == second_index:
        print("Invalid input! Adding additional elements to the board")
        sequence_list.insert(len(sequence_list) // 2, f'-{moves}a')
        sequence_list.insert(len(sequence_list) // 2, f'-{moves}a')
    elif sequence_list[first_index] == sequence_list[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_list[first_index]}!")
        if first_index > second_index:
            sequence_list.pop(first_index)
            sequence_list.pop(second_index)
        else:
            sequence_list.pop(second_index)
            sequence_list.pop(first_index)
    elif sequence_list[first_index] != sequence_list[second_index]:
        print("Try again!")
        command = input()
        continue
    if len(sequence_list) == 0:
        is_solved = True
        print(f"You have won in {moves} turns!")
        break
    command = input()
sequence_list = list(map(str, sequence_list))
if not is_solved:
    print(f"Sorry you lose :(\n{' '.join(sequence_list)} ")
