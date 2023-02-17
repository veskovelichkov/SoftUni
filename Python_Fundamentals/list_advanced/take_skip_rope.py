input_string = input()
string_list = list(input_string.strip(""))
numbers_list = [number for number in string_list if number.isdigit()]
non_numbers_list = [number for number in string_list if not number.isdigit()]
take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0]
new_list = []
counter = 0
for index in range(len(take_list)):
    take_index = int(take_list[index])
    skip_index = int(skip_list[index])
    new_list += non_numbers_list[0:take_index]
    non_numbers_list = non_numbers_list[take_index + skip_index:]

print(''.join(new_list))
