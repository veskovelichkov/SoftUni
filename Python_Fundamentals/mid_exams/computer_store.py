command=input()
price_no_taxes=0
taxes=0
while command!='special' and command!='regular':
    price=float(command)
    if price<0:
        print('Invalid price!')
        command = input()
        continue
    price_no_taxes+=price
    taxes+=0.2*price
    command=input()
if price_no_taxes==0:
    print("Invalid order!")
elif command=="regular":
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_no_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_no_taxes+taxes:.2f}$")
elif command=='special':
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_no_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {(price_no_taxes + taxes)*0.9:.2f}$")