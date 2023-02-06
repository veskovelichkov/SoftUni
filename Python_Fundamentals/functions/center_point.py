import math

def calculate_closest_point(a1, a2, b1, b2):
    if (abs(a1) + abs(a2)) <= (abs(b1) + abs(b2)):
        return f'({math.floor(a1)}, {math.floor(a2)})'
    else:
        return f'({math.floor(b1)}, {math.floor(b2)})'


a_x = float(input())
a_y = float(input())
b_x = float(input())
b_y = float(input())
closer_point=calculate_closest_point(a_x,a_y,b_x,b_y)
print(closer_point)
