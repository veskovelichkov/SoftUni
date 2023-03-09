words_to_remove = input().split(", ")
text = input()
for word in words_to_remove:
    while word in text:
        text = text.replace(word, '*' * len(word))
print(text)
