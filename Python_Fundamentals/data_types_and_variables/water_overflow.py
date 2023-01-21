number=int(input())
capacity=255
for _ in range(number):
    pour=int(input())
    if pour<=capacity:
        capacity-=pour
    else:
        print("Insufficient capacity!")
        continue
print(255-capacity)