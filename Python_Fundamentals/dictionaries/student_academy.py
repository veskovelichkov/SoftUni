number_of_pairs = int(input())
my_dict = {}
for _ in range(number_of_pairs):
    student = input()
    grade = float(input())
    if student not in my_dict:
        my_dict[student] = []
    my_dict[student].append(grade)
new_dict = {key: sum(value) / len(value) for (key, value) in my_dict.items() if sum(value) / len(value) >= 4.5}
for key, value in new_dict.items():
    print(f"{key} -> {value:.2f}")
