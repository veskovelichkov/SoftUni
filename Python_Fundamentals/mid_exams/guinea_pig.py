food=float(input())
hay=float(input())
cover=float(input())
guinea=float(input())
food*=1000
hay*=1000
cover*=1000
guinea*=1000
for i in range(1,31):
    food-=300
    if i%2==0:
        hay-=0.05*food
    if i%3==0:
        cover-=guinea/3
if food>=0 and hay>=0 and cover>=0:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
else:
    print("Merry must go to the pet store!")