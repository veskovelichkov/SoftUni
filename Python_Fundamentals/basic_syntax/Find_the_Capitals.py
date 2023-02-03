string=input()
list=[]
for i in range(len(string)):
    if string[i].isupper():
        list.append(i)
print(list)