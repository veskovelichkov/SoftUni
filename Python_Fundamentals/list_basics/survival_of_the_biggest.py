string=input()
number=int(input())
my_list=string.split(" ")
manipulated_list=[int(my_list[j]) for j in range(len(my_list))]
for i in range(number):
    smallest_number=manipulated_list[0]
    for value in manipulated_list:
        if value<smallest_number:
            smallest_number=value
    manipulated_list.remove(smallest_number)
manipulated_list=[str(manipulated_list[v]) for v in range(len(manipulated_list))]
print(", ".join(manipulated_list))