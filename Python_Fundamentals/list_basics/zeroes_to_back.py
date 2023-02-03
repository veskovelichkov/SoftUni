integers_string=input().split(", ")
integers_int=[]
for value in integers_string:
    integers_int.append(int(value))
sorted_list=[]
for int in integers_int:
    if int!=0:
        sorted_list.append(int)
for _ in range(len(integers_int)-len(sorted_list)):
    sorted_list.append(0)
print(sorted_list)