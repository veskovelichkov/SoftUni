n=int(input())
for _ in range(n):
    i=int(input())
    if i%2!=0:
        print(f'{i} is odd!')
        break
else:
    print("All numbers are even.")