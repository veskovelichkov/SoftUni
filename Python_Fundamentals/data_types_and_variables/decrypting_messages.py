key=int(input())
lines=int(input())
message=''
for _ in range(lines):
    character=input()
    message+=chr(ord(character)+key)
print(message)