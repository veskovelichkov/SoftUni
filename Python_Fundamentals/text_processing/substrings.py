word_to_remove = input()
string_to_check = input()
while word_to_remove in string_to_check:
    string_to_check = string_to_check.replace(word_to_remove, '')
print(string_to_check)
