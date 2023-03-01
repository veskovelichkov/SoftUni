import math

biscuits_per_worker = int(input())
workers_count = int(input())
other_company_biscuits = int(input())
biscuits_produced = 0
for day in range(1, 31):
    biscuits_per_day = biscuits_per_worker * workers_count
    if day % 3 == 0:
        biscuits_per_day = math.floor(biscuits_per_day * 0.75)
    biscuits_produced += biscuits_per_day
print(f"You have produced {biscuits_produced} biscuits for the past month.")
difference = abs((biscuits_produced - other_company_biscuits)/other_company_biscuits)*100
if biscuits_produced>other_company_biscuits:
    print(f"You produce {difference:.2f} percent more biscuits.")
else:
    print(f"You produce {difference:.2f} percent less biscuits.")