number = int(input())
my_dict = {}
for _ in range(number):
    word = input()
    synonym = input()
    if word not in my_dict.keys():
        my_dict[word] = []
    my_dict[word].append(synonym)
for key, value in my_dict.items():
    print(f"{key} - {', '.join(value)}")
