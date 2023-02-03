cards=input()
shuffles=int(input())
initial_list=cards.split(" ")
for _ in range(shuffles):
    shuffled_list = []
    for i in range(int(len(initial_list)//2)):
        shuffled_list.append(initial_list[i])
        shuffled_list.append(initial_list[i+int(len(initial_list)//2)])
    initial_list=shuffled_list
print(initial_list)