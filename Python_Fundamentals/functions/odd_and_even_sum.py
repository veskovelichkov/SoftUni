def calculate_sum_digits(num):
    odd_sum = 0
    even_sum = 0
    for digit in num:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return even_sum, odd_sum


number = input()
even_sum_digits,odd_sum_digits =calculate_sum_digits(number)
print(f'Odd sum = {odd_sum_digits}, Even sum = {even_sum_digits}')