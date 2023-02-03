number=int(input())
positives_list=list()
negatives_list=list()
count_positives=0
sum_negatives=0
for _ in range(number):
    current_number=int(input())
    if current_number<0:
        negatives_list.append(current_number)
        sum_negatives+=current_number
    else:
        positives_list.append(current_number)
        count_positives+=1
print(positives_list)
print(negatives_list)
print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_negatives}')