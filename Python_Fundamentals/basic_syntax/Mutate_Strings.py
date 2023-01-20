first_string=input()
second_string=input()
new_word=''
for index in range(len(first_string)):
    new_word=second_string[:index+1]+first_string[index+1:]
    if first_string[index]==second_string[index]:
        continue
    else:
        print(new_word)