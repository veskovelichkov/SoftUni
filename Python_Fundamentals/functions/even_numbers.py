sequence_of_numbers = list(map(int, input().split(" ")))
even_numbers_list = filter(lambda x: x % 2 == 0, sequence_of_numbers)
print(list(even_numbers_list))
