text = input()
for index in range(len(text)):
    if text[index] == ":" and index + 1 in range(len(text)):
        print(f"{text[index]}{text[index + 1]}")
