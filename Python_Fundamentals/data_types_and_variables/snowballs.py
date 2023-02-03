number_snowballs=int(input())
highest_weight=0
highest_time=0
highest_quality=0
highest_value=0
for _ in range(number_snowballs):
    current_weight=int(input())
    current_time=int(input())
    current_quality=int(input())
    if (current_weight/current_time)**current_quality>highest_value:
        highest_weight=current_weight
        highest_time=current_time
        highest_quality=current_quality
        highest_value=(current_weight/current_time)**current_quality
print(f"{highest_weight} : {highest_time} = {int(highest_value)} ({highest_quality})")
