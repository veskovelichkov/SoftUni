def calculator(command,a,b):
    if command=='multiply':
        return a*b
    elif command=='divide':
        return int(a/b)
    elif command=='add':
        return a+b
    elif command=='subtract':
        return a-b
input_operator=input()
first_num=int(input())
second_num=int(input())
print(calculator(input_operator,first_num,second_num))