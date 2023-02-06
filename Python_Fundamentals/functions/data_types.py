def data_types(type, word):
    if type == 'int':
        return int(word) * 2
    elif type == 'real':
        return f'{float(word) * 1.5:.2f}'
    elif type == 'string':
        return f'${word}$'


current_type = input()
current_word = input()
current_output = data_types(current_type, current_word)
print(current_output)
