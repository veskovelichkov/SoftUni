employees_happiness = list(map(int, input().split(' ')))
factor = int(input())
improved_happiness = list(map(lambda x: x * factor, employees_happiness))
improved_happiness = list(
    filter(lambda x: x >= (sum(improved_happiness) / len(improved_happiness)), improved_happiness))
if len(improved_happiness) * 2 >= len(employees_happiness):
    print(f"Score: {len(improved_happiness)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(improved_happiness)}/{len(employees_happiness)}. Employees are not happy!")
