def circle(r):
    pi = 3.14
    area = pi * (r ** 2)
    circumference = 2 * pi * r
    
    return area, circumference

r = int(input())

area, circumference = circle(r)

print('반지름이 {}인 원의 넓이는 {}, 원주는 {}입니다.'.format(r,area, circumference))
