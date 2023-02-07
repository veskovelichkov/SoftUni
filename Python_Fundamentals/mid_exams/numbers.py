sequence_list = list(map(int, input().split(" ")))
avg = sum(sequence_list) / len(sequence_list)
above_average_list = sorted([x for x in sequence_list if x > avg], reverse=True)
above_average_list_strings = list(map(str, above_average_list))
if len(above_average_list_strings) == 0:
    print("No")
elif len(above_average_list_strings) < 5:
    print(' '.join(above_average_list_strings))
else:
    print(' '.join(above_average_list_strings[:5]))
