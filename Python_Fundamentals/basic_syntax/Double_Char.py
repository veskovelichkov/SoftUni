while True:
    word=input()
    if word=='End':
        break
    if word=='SoftUni':
        continue
    for ch in word:
        print(2*ch,end='')
    print()
