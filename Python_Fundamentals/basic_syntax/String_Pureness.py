n=int(input())
for _ in range(n):
    string=input()
    is_pure=True
    for ch in string:
        if ch==',' or ch=='.' or ch=='_':
            is_pure=False
            break
    if is_pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')