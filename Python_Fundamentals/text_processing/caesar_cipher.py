text = input()
new_text = ''
for character in text:
    new_char = chr(ord(character) + 3)
    new_text += new_char
print(new_text)
