country = input().split(", ")
capital = input().split(", ")
new_dict = dict(zip(country, capital))
for key,value in new_dict.items():
    print(f"{key} -> {value}")