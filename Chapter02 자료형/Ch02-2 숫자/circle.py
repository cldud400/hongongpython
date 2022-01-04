def circle(r):
    pi = 3.14
    area = pi * (r ** 2)
    circumference = 2 * pi * r
    
    return area, circumference

r = int(input())

area, circumference = circle(r)

print(area, circumference)
