electrons = int(input())
distribution = []
electrons_sorted = 0
counter = 0
while True:
    counter += 1
    if electrons_sorted + 2 * (counter ** 2) < electrons:
        distribution.append(2 * (counter ** 2))
        electrons_sorted += 2 * (counter ** 2)
    else:
        distribution.append(electrons - electrons_sorted)
        break
print(distribution)
