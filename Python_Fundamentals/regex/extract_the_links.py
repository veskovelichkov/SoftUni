import re

line = input()
pattern = r'(www\.([a-z0-9A-Z\-]+)\.[a-z]+(\.[a-z]+)*)'
while line:
    result = re.search(pattern, line)
    if result:
        print(result.group(1))
    line = input()
