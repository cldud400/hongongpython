numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99, -100, -9999, 9999, 100, 0]
# 실행 결과
#273 은(는) 3자리수 입니다.

for i in numbers:
    origin_num = i
    tmp = abs(i)
    cnt = 0
    while True:
        tmp = (tmp // 10)
        cnt += 1     
        if tmp == 0:
            break 
    print(f'{origin_num}은(는) {cnt}자리수 입니다.')