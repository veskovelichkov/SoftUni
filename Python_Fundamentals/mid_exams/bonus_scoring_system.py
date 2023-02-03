import math
students=int(input())
lectures=int(input())
bonus=int(input())
max_bonus=0
max_attendences=0
for student in range(students):
    attendences=int(input())
    total_bonus=attendences/lectures*(5+bonus)
    if total_bonus>max_bonus:
        max_bonus=total_bonus
        max_attendences=attendences
print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendences} lectures.")