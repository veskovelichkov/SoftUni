def factorial_division(number):
    factorial_number = 1
    for i in range(1, number + 1):
        factorial_number *= i
    return factorial_number


first_number = int(input())
second_number = int(input())
first_factorial = factorial_division(first_number)
second_factorial = factorial_division(second_number)
print(f"{first_factorial / second_factorial:.2f}")
