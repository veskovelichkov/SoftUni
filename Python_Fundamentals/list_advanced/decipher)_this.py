words = input().split(" ")

for word in words:
    word_as_list = list(word)
    digits = [digit for digit in word if digit.isdigit()]
    word_as_list = word_as_list[len(digits):]
    number = int(''.join(digits))
    word_as_list.insert(0, chr(number))
    word_as_list[1], word_as_list[-1] = word_as_list[-1], word_as_list[1]
    print("".join(word_as_list), end=" ")
