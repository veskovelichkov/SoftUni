numbers = list(map(int, input().split(", ")))
new_list = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
print(new_list)
