event = input()
my_dict = {}
while event != "end":
    course, student = event.split(" : ")
    if course not in my_dict.keys():
        my_dict[course] = []
    my_dict[course].append(student)
    event = input()
for key, value in my_dict.items():
    print(f"{key}: {len(value)}")
    for item in value:
        print(f"-- {item}")
