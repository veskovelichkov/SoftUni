string=input()
list_of_animals=string.split(", ")
wolf_position=0
for i in range(len(list_of_animals)-1,-1,-1):
    if list_of_animals[i]=='wolf':
        wolf_position=len(list_of_animals)-i
        break
if wolf_position==1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_position-1}! You are about to be eaten by a wolf!")
