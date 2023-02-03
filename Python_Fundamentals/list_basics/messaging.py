numbers_string=input().split(" ")
string=input()
numbers_int=[]
new_string=''
for value in numbers_string:
    sum_number=0
    for digit in value:
        sum_number+=int(digit)
    numbers_int.append(sum_number)
for index in range (len(numbers_int)):
    current_index=numbers_int[index]
    while current_index>len(string):
        current_index-=len(string)
    new_string+=string[current_index]
    string=string[:current_index]+string[current_index+1:]

print(new_string)

