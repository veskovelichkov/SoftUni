palindrome_strings = input().split(" ")
count_palindrome = input()
palindrome_list = [palindrome for palindrome in palindrome_strings if palindrome == palindrome[::-1]]
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(count_palindrome)} times")
