n=int(input())
for i in range(1,n+1):
    sum_digits=0
    for digits in (str(i)):
        sum_digits+=int(digits)
    if sum_digits==5 or sum_digits==7 or sum_digits==11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")