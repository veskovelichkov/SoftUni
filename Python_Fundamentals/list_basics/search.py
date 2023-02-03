lines=int(input())
key_word=input()
whole_list=list()
filtered_list=list()
for _ in range(lines):
    sentence=input()
    whole_list.append(sentence)
for value in (whole_list):
    if key_word in value:
        filtered_list.append(value)
print(whole_list)
print(filtered_list)