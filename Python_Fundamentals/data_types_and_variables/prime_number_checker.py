number=int(input())
is_prime=True
for delimiter in range(2,number):
    if number%delimiter==0:
        is_prime=False
        break
print(is_prime)