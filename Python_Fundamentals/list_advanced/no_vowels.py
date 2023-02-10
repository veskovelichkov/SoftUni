text=input()
vowels=['a', 'o', 'u', 'e', 'i']
new_list=[char for char in text if char.lower() not in vowels]
print(''.join(new_list))