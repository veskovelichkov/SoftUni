def merge(list_of_people, start_index, end_index):
    if start_index<0:
        start_index=0
    elif start_index>=len(list_of_people):
        start_index=len(list_of_people)-1
    if end_index>0:
        end_index=0
    elif end_index>=len(list_of_people):
        end_index=len(list_of_people)-1
    if start_index in range(len(list_of_people)) and end_index in range(len(list_of_people)):
        new_string=''.join(list_of_people[start_index:end_index+1])
        list_of_people=list_of_people[0:start_index]+list_of_people[end_index+1:]
        list_of_people.insert(start_index,new_string)
    return list_of_people


threat_people = list(map(str, input().split(" ")))
while True:
    command = input()
    if command == "3:1":
        break
    command_as_list = command.split(" ")
    event = command_as_list[0]
    start_index_index=int(command_as_list[1])
    end_index_partitions=int(command_as_list[2])
    if event=="merge":
        threat_people=merge(threat_people,start_index_index,end_index_partitions)
    elif event=="divide":
        threat_people=merge(threat_people,start_index_index,end_index_partitions)
print(threat_people)