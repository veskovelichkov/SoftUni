lines=int(input())
COMMAND_EVEN='even'
COMMAND_ODD='odd'
COMMAND_NEGATIVE='negative'
COMMAND_POSITIVE='positive'
all_numbers=list()
for _ in range(lines):
    number=int(input())
    all_numbers.append(number)
command=input()
filtered_list=list()
for value in all_numbers:
    passed_tests=(
        (command==COMMAND_EVEN and value%2==0) or
        (command==COMMAND_ODD and value%2!=0) or
        (command==COMMAND_POSITIVE and value>=0) or
        (command==COMMAND_NEGATIVE and value<0)
    )
    if passed_tests:
        filtered_list.append(value)
print(filtered_list)