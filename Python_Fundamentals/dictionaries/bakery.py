products = input().split()
bakery = {}
for i in range(0, len(products), 2):
    bakery[products[i]] = int(products[i + 1])
print(bakery)
