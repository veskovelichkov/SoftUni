values = list(map(float, input().split(" ")))
new_list=[]
for value in values:
    new_list.append(abs(value))
print(new_list)