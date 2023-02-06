def characters_in_range(first, second):
    resulting_list = []
    for value in range(ord(first)+1, ord(second)):
        resulting_list.append(chr(value))
    return (' '.join(resulting_list))


first_char = input()
second_char = input()
result = characters_in_range(first_char, second_char)
print(result)
