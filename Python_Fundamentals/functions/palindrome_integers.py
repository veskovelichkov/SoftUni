def check_palindrome(seq_num):
    list_numbers = seq_num.split(', ')
    is_palindrome = []
    for value in list_numbers:
        if value == value[::-1]:
            is_palindrome.append("True")
        else:
            is_palindrome.append("False")
    return is_palindrome


sequence_numbers = input()
result = check_palindrome(sequence_numbers)
print('\n'.join(result))
