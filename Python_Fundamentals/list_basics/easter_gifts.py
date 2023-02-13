def outofstock(sequence, chosen_gift):
    sequence = list(map(lambda x: x.replace(chosen_gift, "None"), sequence))
    return sequence


def required(sequence, chosen_gift, chosen_index):
    if chosen_index in range(len(sequence)):
        sequence[chosen_index] = chosen_gift
    return sequence


def justincase(sequence, chosen_gift):
    sequence[-1] = chosen_gift
    return sequence


gifts = list(map(str, input().split(" ")))
while True:
    command = input()
    if command == "No Money":
        break
    command_split = command.split(" ")
    event = command_split[0]
    gift = command_split[1]
    if event == "OutOfStock":
        gifts = outofstock(gifts, gift)
    elif event == "Required":
        index = int(command_split[2])
        gifts = required(gifts, gift, index)
    elif event == "JustInCase":
        gifts = justincase(gifts, gift)
gifts=[value for value in gifts if value!="None"]
print(" ".join(gifts))
