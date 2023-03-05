my_dict = {}
while True:
    current_recourse = input()
    if current_recourse == "stop":
        break
    current_quantity = int(input())
    if current_recourse not in my_dict:
        my_dict[current_recourse] = 0
    my_dict[current_recourse] += current_quantity
for resource, quantity in my_dict.items():
    print(f"{resource} -> {quantity}")
