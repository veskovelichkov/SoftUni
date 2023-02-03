tail=input()
body=input()
head=input()
empty_list=list()
empty_list.append(tail)
empty_list.append(body)
empty_list.append(head)
empty_list[0],empty_list[2] = empty_list[2],empty_list[0]
print(empty_list)