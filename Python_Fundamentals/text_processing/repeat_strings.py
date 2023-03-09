sequence_strings = input().split(" ")
new_string = ''
for word in sequence_strings:
    new_string += word * (len(word))
print(new_string)
