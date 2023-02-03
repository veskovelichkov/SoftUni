string=input()
initial_list=string.split(" ")
list_int=list()
for value in initial_list:
    value=-int(value)
    list_int.append(value)
print(list_int)