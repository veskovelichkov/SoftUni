days=int(input())
daily_plunder=int(input())
expected_plunder=float(input())
gathered_blunder=0
for day in range(1,days+1):
    gathered_blunder+=daily_plunder
    if day%3==0:
        gathered_blunder+=daily_plunder/2
    if day%5==0:
        gathered_blunder*=0.7
if gathered_blunder>=expected_plunder:
    print(f"Ahoy! {gathered_blunder:.2f} plunder gained.")
else:
    percentage_gathered=gathered_blunder/expected_plunder*100
    print(f"Collected only {percentage_gathered:.2f}% of the plunder.")
