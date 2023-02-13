sequence_list = list(map(int, input().split(", ")))
boundary = 0
while sequence_list:
    boundary+=10
    new_list=[]
    for value in sequence_list:
        if value<=boundary:
            new_list.append(value)
    sequence_list=[number for number in sequence_list if number not in new_list]
    print(f"Group of {boundary}'s: {new_list}")