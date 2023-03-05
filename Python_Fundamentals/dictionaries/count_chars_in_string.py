text = input().split()
string = ''.join(text)
my_dict = {}
for char in string:
    if char not in my_dict:
        my_dict[char] = 0
    my_dict[char] += 1
for char, occurrences in my_dict.items():
    print(f"{char} -> {occurrences}")
