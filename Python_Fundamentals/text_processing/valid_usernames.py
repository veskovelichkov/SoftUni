def check_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def valid_character(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == '_'):
            return False
    return True


def no_reduntant_symbols(name):
    if " " in name:
        return False
    return True


def is_valid(name):
    if check_length(name) and valid_character(name) and no_reduntant_symbols(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if is_valid(username):
        print(username)
