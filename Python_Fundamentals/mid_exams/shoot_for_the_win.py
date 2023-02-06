sequence_list = list(map(int, input().split(' ')))
command = input()
counter = 0
indexes_hit = []
while command != 'End':
    index = int(command)
    if index >= len(sequence_list):
        command = input()
        continue
    if index in indexes_hit:
        continue
    indexes_hit.append(index)
    counter += 1
    for i in range(0, len(sequence_list)):
        if i == index:
            continue
        if i in indexes_hit:
            continue
        if sequence_list[i] > sequence_list[index]:
            sequence_list[i] -= sequence_list[index]
        else:
            sequence_list[i] += sequence_list[index]
    sequence_list[index] = -1
    command = input()
sequence_list = map(str, sequence_list)
print(f'Shot targets: {counter} -> {" ".join(sequence_list)}')
