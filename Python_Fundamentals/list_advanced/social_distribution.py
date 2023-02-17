citizens = list(map(int, input().split(", ")))
minimum = int(input())
if sum(citizens) < minimum * len(citizens):
    print("No equal distribution possible")
else:
    for i in range(len(citizens)):
        maximum = max(citizens)
        index = citizens.index(maximum)
        if citizens[i] < minimum:
            difference = minimum - citizens[i]
            citizens[i] += difference
            citizens[index] -= difference
    print(citizens)
