budget=float(input())
price_flour=float(input())
price_eggs=0.75*price_flour
price_milk=1.25*price_flour
used_money=0
counter_breads=0
counter_eggs=0
while used_money+price_flour+0.25*price_milk+price_eggs<budget:
    used_money+=price_flour+price_eggs+0.25*price_milk
    counter_breads+=1
    counter_eggs+=3
    if counter_breads%3==0:
        counter_eggs=counter_eggs-(counter_breads-2)
print(f"You made {counter_breads} loaves of Easter bread! Now you have {counter_eggs} eggs and {budget-used_money:.2f}BGN left.")