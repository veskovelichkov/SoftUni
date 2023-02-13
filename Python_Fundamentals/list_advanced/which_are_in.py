first_sequence = list(map(str, input().split(", ")))
second_sequence = list(map(str, input().split(", ")))
first_in_second = [string1 for string1 in first_sequence if any(string1 in string2 for string2 in second_sequence)]
print(first_in_second)
