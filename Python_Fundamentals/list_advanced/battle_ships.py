number_of_lines=int(input())
dict={}
for i in range(number_of_lines):
    line=input().split(" ")
    dict+={f"Line {i}":line}
print(dict)