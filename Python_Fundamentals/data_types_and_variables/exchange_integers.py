first_number=int(input())
second_number=int(input())
temporary_number=first_number
first_number=second_number
print(f"""
Before:
a = {temporary_number}
b = {first_number}
After:
a = {first_number}
b = {temporary_number}
""")