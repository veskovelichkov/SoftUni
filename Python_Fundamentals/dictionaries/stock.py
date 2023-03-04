products = input().split()
check_items = input().split()
bakery = {}
for i in range(0, len(products), 2):
    bakery[products[i]] = int(products[i + 1])
for item in check_items:
    if item in bakery.keys():
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
