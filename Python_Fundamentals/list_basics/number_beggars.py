money_list=input().split(", ")
number_beggars=int(input())
money_list_as_digits=[]
for value in money_list:
    money_list_as_digits.append(int(value))
starting_index=0
final_sums=[]
while starting_index<number_beggars:
    sum_of_beggars=0
    for current_index in range(starting_index,len(money_list_as_digits),number_beggars):
        sum_of_beggars+=money_list_as_digits[current_index]
    final_sums.append(sum_of_beggars)
    starting_index+=1
print(final_sums)