import re

line = input()
word = input()
pattern = fr"\b{word}\b"
results = re.findall(pattern, line, re.IGNORECASE)
print(len(results))
