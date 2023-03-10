keys = list(map(int, input().split()))
list_of_messages = []
command = input()
while command != 'find':
    list_of_messages.append(command)
    command = input()
for message in list_of_messages:
    new_message = ''
    current_index = 0
    for index in range(len(message)):
        current_char = message[index]
        new_message += chr(ord(current_char) - keys[current_index])
        current_index += 1
        if current_index >= len(keys):
            current_index = 0
    new_message_split = new_message.split('&')
    last_message = new_message_split[-1].split("<")
    print(f"Found {new_message_split[1]} at {last_message[1][:-1]}")
