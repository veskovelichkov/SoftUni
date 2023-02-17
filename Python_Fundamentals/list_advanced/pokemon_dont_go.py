sequence = list(map(int, input().split(" ")))
sum = 0
while sequence != []:
    index = int(input())
    if index < 0:
        removed = sequence.pop(0)
        last_element = sequence[-1]
        sequence.insert(0, last_element)
    elif index >= len(sequence):
        removed = sequence.pop(-1)
        first_element = sequence[0]
        sequence.append(first_element)
    else:
        removed = sequence.pop(index)
    sum += removed
    for item in range (len(sequence)):
        if removed >= sequence[item]:
            sequence[item] += removed
        else:
            sequence[item] -= removed
print(sum)