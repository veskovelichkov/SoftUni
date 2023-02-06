def check_smallest(first, second, third):
    list_numbers = [first, second, third]
    return min(list_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(check_smallest(first_number, second_number, third_number))
