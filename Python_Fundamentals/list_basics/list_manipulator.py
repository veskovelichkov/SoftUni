initial_list=input().split(" ")
command=input()
new_list=list()
initial_list_int=[]
for value in initial_list:
    initial_list_int.append(int(value))
while command!="end":
    if "exchange" in command:
        command_exchange=command.split(" ")
        index=int(command_exchange[1])
        if index>len(initial_list_int) or index<0:
            print("Invalid index")
            command=input()
            continue
        else:
            initial_list_int=initial_list_int[index+1:]+initial_list_int[:index+1]
    elif "max" in command:
        command_max=command.split(" ")
        odd_even=command_max[1]
        is_found=False
        if odd_even=="even":
            max_even=0
            index_even=0
            for j in range(len(initial_list_int)):
                if initial_list_int[j]%2==0 and initial_list_int[j]>=max_even:
                    max_even=initial_list_int[j]
                    index_even=j
                    is_found=True
            if is_found:
                print(index_even)
            else:
                print("No matches")
        if odd_even=="odd":
            max_odd=0
            index_odd=0
            for i in range(len(initial_list_int)):
                if initial_list_int[i]%2!=0 and initial_list_int[i]>=max_odd:
                    max_odd=initial_list_int[i]
                    index_odd=i
                    is_found=True
            if is_found:
                print(index_odd)
            else:
                print("No matches")
    elif "min" in command:
        command_min=command.split(" ")
        odd_even=command_min[1]
        is_found=False
        if odd_even=="even":
            min_even=1000
            index_even=0
            for j in range(len(initial_list_int)):
                if initial_list_int[j]%2==0 and initial_list_int[j]<=min_even:
                    min_even=initial_list_int[j]
                    index_even=j
                    is_found=True
            if is_found:
                print(index_even)
            else:
                print("No matches")
        if odd_even=="odd":
            min_odd=1000
            index_odd=0
            for i in range(len(initial_list_int)):
                if initial_list_int[i]%2!=0 and initial_list_int[i]<=min_odd:
                    min_odd=initial_list_int[i]
                    index_even=i
                    is_found=True
            if is_found:
                print(min_odd)
            else:
                print("No matches")
    elif "first" in command:
        command_first=command.split(" ")
        count=int(command_first[1])
        odd_even=command_first[2]
        if count>len(initial_list_int):
            print("Invalid count")
            command=input()
            continue
        if odd_even=="even":
            list_even=[]
            counter=0
            for i in range(len(initial_list_int)):
                if initial_list_int[i]%2==0:
                    list_even.append(initial_list_int[i])
                    counter+=1
                if counter==count:
                    break
            print(list_even)
        elif odd_even=='odd':
            list_odd = []
            counter = 0
            for i in range(len(initial_list_int)):
                if initial_list_int[i] % 2 != 0:
                    list_odd.append(initial_list_int[i])
                    counter += 1
                if counter == count:
                    break
            print(list_odd)
    elif "last" in command:
        command_first = command.split(" ")
        count = int(command_first[1])
        odd_even = command_first[2]
        if count > len(initial_list_int):
            print("Invalid count")
            command = input()
            continue
        if odd_even == "even":
            list_even = []
            counter = 0
            for i in range(len(initial_list_int)-1,-1,-1):
                if counter == count:
                    break
                if initial_list_int[i] % 2 == 0:
                    list_even.append(initial_list_int[i])
                    counter += 1
            print(list_even)
        elif odd_even == 'odd':
            list_odd = []
            counter = 0
            for i in range(len(initial_list_int)-1,-1,-1):
                if counter == count:
                    break
                if initial_list_int[i] % 2 != 0:
                    list_odd.append(initial_list_int[i])
                    counter += 1
            print(list_odd)
    command=input()
print(initial_list_int)