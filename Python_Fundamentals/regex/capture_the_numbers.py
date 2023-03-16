import re

line = input()
pattern = r'\d+'
while line:
    result = re.findall(pattern, line)
    for res in result:
        print(res, end=' ')
    line = input()
