string = input()
new_string = ''
explosion_strenght = 0
for index in range(len(string)):
    if explosion_strenght > 0 and string[index] != ">":
        explosion_strenght -= 1
    elif string[index] == ">" and index + 1 in range(len(string) - 1):
        new_string += '>'
        explosion_strenght += int(string[index + 1])
    else:
        new_string += string[index]
print(new_string)
