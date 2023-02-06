def tribonacci_sequence(num):
    if num==1:
        return [1]
    if num==2:
        return [1,1]
    tribonacci_list = [1, 1, 2]
    for i in range(3, num):
        sum_prv_three = tribonacci_list[i - 1] + tribonacci_list[i - 2] + tribonacci_list[i - 3]
        tribonacci_list.append(sum_prv_three)
    return tribonacci_list


number_of_inputs = int(input())
sequence=tribonacci_sequence(number_of_inputs)
sequence=map(str,sequence)
print(' '.join(sequence))
