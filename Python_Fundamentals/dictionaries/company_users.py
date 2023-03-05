my_dict = {}
company_user = input()
while company_user != "End":
    company_name, employee_id = company_user.split(" -> ")
    if company_name not in my_dict:
        my_dict[company_name] = []
    if employee_id not in my_dict[company_name]:
        my_dict[company_name].append(employee_id)
    company_user = input()
for key, value in my_dict.items():
    print(key)
    for item in value:
        print(f"-- {item}")
