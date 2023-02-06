def check_calculation(order,amount):
    if order=='coffee':
        return f'{amount*1.5:.2f}'
    elif order=='water':
        return f'{amount*1.00:.2f}'
    elif order=='coke':
        return f'{amount*1.40:.2f}'
    elif order=='snacks':
        return f'{amount*2.00:.2f}'
drink=input()
quantity=int(input())
print(check_calculation(drink,quantity))