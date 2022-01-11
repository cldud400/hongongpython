from math import pi as PI

def number_input():
    output = input('숫자 입력 > ')
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def ger_circle_area(radius):
    return PI * (radius ** 2)
