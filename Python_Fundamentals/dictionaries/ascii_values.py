letters = input().split(", ")
my_dict = {}
for letter in letters:
    if letter not in my_dict.keys():
        my_dict[letter] = ord(letter)
print(my_dict)
