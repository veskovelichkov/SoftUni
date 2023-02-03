n=int(input())
total=0
for _ in range(n):
    price_per_capsule=float(input())
    days=int(input())
    capsules=int(input())
    if price_per_capsule<0.01 or price_per_capsule>100:
        continue
    if days<1 or days>31:
        continue
    if capsules<1 or capsules>2000:
        continue
    order=price_per_capsule*days*capsules
    total+=price_per_capsule*days*capsules
    print(f"The price for the coffee is: ${order:.2f}")
print(f'Total: ${total:.2f}')