def perfect_number(num):
    is_perfect = False
    sum_divisor = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_divisor += divisor
    if num == sum_divisor:
        is_perfect = True
    return is_perfect

number = int(input())
check_perfect = perfect_number(number)
if check_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
