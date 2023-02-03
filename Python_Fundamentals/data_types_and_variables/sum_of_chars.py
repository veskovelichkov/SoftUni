number_of_chars=int(input())
sum=0
for _ in range(number_of_chars):
    character=input()
    sum+=ord(character)
print(f"The sum equals: {sum}")