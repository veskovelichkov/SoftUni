number_of_lines = int(input())
for _ in range(number_of_lines):
    person = input().split(" ")
    age = 0
    name = ''
    for information in person:
        if "@" in information and "|" in information and information.index("@")<information.index("|"):
            first_index = information.index("@")
            last_index = information.index("|")
            name = information[first_index + 1:last_index]
        elif "#" in information and "*" in information and information.index("#")<information.index("*"):
            first_index = information.index("#")
            last_index = information.index("*")
            age = information[first_index + 1:last_index]
    print(f"{name} is {age} years old.")
