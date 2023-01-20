budget=int(input())
command=input()
basket=0
while command!="End":
    product=int(command)
    basket+=product
    if basket>budget:
        print("You went in overdraft!")
        break
    command=input()
else:
    print("You bought everything needed.")