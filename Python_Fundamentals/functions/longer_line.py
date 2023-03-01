import math


def calculate_longer_line(a1, a2, a3, a4, b1, b2, b3, b4):
    length_first_line = math.sqrt((abs(a1) + abs(a3)) ** 2 + (abs(a2) + abs(a4)) ** 2)
    length_second_line = math.sqrt((abs(b1) + abs(b3)) ** 2 + (abs(b2) + abs(b4)) ** 2)
    if length_first_line < length_second_line:
        if abs(b1) + abs(b2) <= abs(b3) + abs(b4):
            return f"({b1:.0f}, {b2:.0f})({b3:.0f}, {b4:.0f})"
        else:
            return f"({b3:.0f}, {b4:.0f})({b1:.0f}, {b2:.0f})"
    else:
        if abs(a1) + abs(a2) <= abs(a3) + abs(a4):
            return f"({a1:.0f}, {a2:.0f})({a3:.0f}, {a4:.0f})"
        else:
            return f"({a3:.0f}, {a4:.0f})({a1:.0f}, {a2:.0f})"


a_x1 = float(input())
a_y1 = float(input())
a_x2 = float(input())
a_y2 = float(input())
b_x1 = float(input())
b_y1 = float(input())
b_x2 = float(input())
b_y2 = float(input())
print(calculate_longer_line(a_x1,a_y1,a_x2,a_y2,b_x1,b_y1,b_x2,b_y2))