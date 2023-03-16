import re
line=input()
furniture_list=[]
money_spend=0
pattern=r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
while line!="Purchase":
    result=re.search(pattern,line)
    if result:
        furniture,price,quantity=result.groups()
        furniture_list.append(furniture)
        money_spend+=float(price)*int(quantity)
    line=input()
print("Bought furniture:")
if furniture_list:
    print("\n".join(furniture_list))
print(f"Total money spend: {money_spend:.2f}")