first_line=input().split(" ")
second_line=input().split(" ")
third_line=input().split(" ")
for i in range(3):
    if first_line[i] == second_line[i]== third_line[i]:
        if first_line[i] == "1":
            print("First player won!")
        elif first_line[i] == "2":
            print("Second player won!")
