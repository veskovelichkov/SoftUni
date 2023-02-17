def is_zero(first, second, third):
    zero_found = False
    if first == 0 or second == 0 or third == 0:
        zero_found = True
    return zero_found


def is_negative(first, second, third):
    counter_negative = 0
    negative_found = False
    if first != abs(first):
        counter_negative += 1
    if second != abs(second):
        counter_negative += 1
    if third != abs(third):
        counter_negative += 1
    if counter_negative == 1 or counter_negative == 3:
        negative_found = True
    return negative_found


first_number = int(input())
second_number = int(input())
third_number = int(input())
if is_zero(first_number, second_number, third_number):
    print("zero")
elif is_negative(first_number, second_number, third_number):
    print("negative")
else:
    print("positive")
