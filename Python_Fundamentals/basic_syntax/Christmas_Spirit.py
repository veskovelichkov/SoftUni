quantity=int(input())
days=int(input())
money_spent=0
points=0
for i in range(1,days+1):
    if i%11==0:
        quantity+=2
    if i%2==0:
        money_spent+=quantity*2
        points+=5
    if i%3==0:
        money_spent+=8*quantity
        points+=13
    if i%5==0:
        money_spent+=15*quantity
        points+=17
    if i%10==0:
        money_spent+=23
        points-=20
    if i%15==0:
        points+=30
if days%10==0:
    points-=30
print(f"Total cost: {money_spent}")
print(f"Total spirit: {points}")