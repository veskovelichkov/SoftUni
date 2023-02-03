year=int(input())
while True:
    year += 1
    string_year = str(year)
    empty_set=set()
    for i in range(len(string_year)):
        empty_set.add(string_year[i])
    if len(empty_set)==len(string_year):
        print(year)
        break