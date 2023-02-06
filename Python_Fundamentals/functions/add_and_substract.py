def sum_numbers(first, second):
    return first + second


def substract(sum, third):
    return sum - third


def add_and_subtract(first, second, third):
    sum_first_second = sum_numbers(first, second)
    result = substract(sum_first_second, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
resulting_number = add_and_subtract(first_number, second_number, third_number)
print(resulting_number)
