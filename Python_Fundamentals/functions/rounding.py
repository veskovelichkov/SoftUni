initial_list=list(map(float,input().split(" ")))
rounded_list=[]
for value in initial_list:
    rounded_list.append(round(value))
print(rounded_list)