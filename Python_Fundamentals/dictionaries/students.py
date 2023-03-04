student = input().split(":")
students_dict = {}
while len(student) > 1:
    name, id, course = student[0], student[1], student[2]
    if course not in students_dict.keys():
        students_dict[course] = []
    students_dict[course].append([name, id])
    student = input().split(":")
student = student[0].replace("_", " ")
for item in students_dict[student]:
    print(f"{item[0]} - {item[1]}")
