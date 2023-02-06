import math

def calculate_closest_line(a1, a2,a3,a4, b1, b2,b3,b4):
    length_first_line=math.sqrt((abs(a1)+abs(a3))**2+(abs(a2)+abs(a4))**2)
    length_second_line=math.sqrt((abs(b1)+abs(b3))**2+(abs(b2)+abs(b4))**2)
    if length_first_line<=length_second_line:



a_x1 = float(input())
a_y1 = float(input())
a_x2 = float(input())
a_y2 = float(input())
b_x1 = float(input())
b_y1 = float(input())
b_x2 = float(input())
b_x2 = float(input())

