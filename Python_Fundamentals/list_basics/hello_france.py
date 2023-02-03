items=input().split("|")
budget=float(input())
bought_items_list=[]
sold_items=0
profit=0
for item_price in items:
    item_price_split=item_price.split("->")
    item=item_price_split[0]
    price=float(item_price_split[1])
    if (item=='Clothes' and price<=50) or (item=='Shoes' and price<=35) or (item=='Accessories' and price<=20.5):
        if price<=budget:
            budget-=price
            sell_price=1.4*price
            profit+=0.4*price
            sold_items+=1.4*price
            bought_items_list.append(sell_price)
        else:
            continue
    else:
        continue
for i in bought_items_list:
    print(f"{i:.2f}",end=' ')
print()
print(f"Profit: {profit:.2f}")
if budget+sold_items>=150:
    print("Hello, France!")
else:
    print("Not enough money.")