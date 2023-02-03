gifts_string=input()
gifts_list=gifts_string.split(" ")
command=input()
while command!='No Money':
    command_list=command.split(" ")
    if len(command_list)==2:
        if command_list[0]=="OutOfStock":
            gifts_list=[w.replace(command_list[1],"None") for w in gifts_list]
        elif command_list[0]=="JustInCase":
            gifts_list[-1]=command_list[1]
    elif len(command_list)==3:
        if command_list[0]=="Required":
            index=int(command_list[-1])
            gifts_list[index-1]=command_list[1]
    command=input()
gifts_list_updated=[v for v in gifts_list if v!="None"]
print(" ".join(gifts_list_updated))