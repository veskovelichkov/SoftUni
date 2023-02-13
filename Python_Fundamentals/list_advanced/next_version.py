current_version = list(map(int, input().split(".")))
current_version[-1]+=1
for current_index in range(len(current_version)-1,-1,-1):
    if current_version[current_index]>9:
        current_version[current_index]=0
        if current_index-1 in range (len(current_version)):
            current_version[current_index-1]+=1
print('.'.join(list(map(str, current_version))))
