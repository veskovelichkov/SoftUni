fire_events=input().split('#')
water_amount=int(input())
effort=0
total_fire=0
cells_extinguished=[]
for fires in fire_events:
    events=fires.split(" = ")
    type=events[0]
    range=int(events[1])
    if (type=='Low' and range>=1 and range<=50) or (type=='Medium' and range>=51 and range<=80) or (type=='High' and range>=81 and range<=125):
        if water_amount>=range:
            cells_extinguished.append(range)
            water_amount-=range
            effort+=0.25*range
            total_fire+=range
    else:
        continue
print("Cells:")
for value in cells_extinguished:
    print(f" - {value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")