messages = input().split()
messages_stripped = [message.strip() for message in messages]
total_sum = 0
for message in messages_stripped:
    first_letter = message[0]
    last_letter = message[-1]
    current_number = int(message[1:-1])
    if first_letter.isupper():
        current_number = current_number / (ord(first_letter) - 64)
    else:
        current_number = current_number * (ord(first_letter) - 96)
    if last_letter.isupper():
        current_number = current_number - (ord(last_letter) - 64)
    else:
        current_number = current_number + (ord(last_letter) - 96)
    total_sum += current_number
print(f"{total_sum:.2f}")
