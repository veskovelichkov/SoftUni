import re

text = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\-\_\.]*)@[a-z\-]+(\.[a-z]+)+)"
result = re.findall(pattern, text)
for group in result:
    print(group[0])
