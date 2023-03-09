message = input()
my_list = []
new_string = ''
output = ''
for index in range(len(message)):
    if not message[index].isnumeric():
        new_string += message[index].upper()
        if message[index].upper() not in my_list:
            my_list.append(message[index].upper())
    else:
        if index + 1 in range(len(message)) and message[index + 1].isdigit():
            repeat = 10 * int(message[index]) + int(message[index + 1])
        else:
            repeat = int(message[index])
        output += new_string * repeat
        new_string = ''
print(f"Unique symbols used: {len(my_list)}")
print(output)
