first_employee=int(input())
second_employee=int(input())
third_employee=int(input())
students=int(input())
counter=0
students_helped=0
hours_needed=0
while students_helped<students:
    counter+=1
    hours_needed+=1
    if counter==4:
        counter=0
        continue
    students_helped+=first_employee+second_employee+third_employee
print(f"Time needed: {hours_needed}h.")
