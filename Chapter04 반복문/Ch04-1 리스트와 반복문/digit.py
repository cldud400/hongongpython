numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99, -100, -9999, 9999, 100, 0]
# 실행 결과
#273 은(는) 3자리수 입니다.

for i in numbers:
    num_ = i
    i = abs(i)
    n = 0
    while True:
        i = (i // 10)
        n += 1     
        if i == 0:
            break 
    print(f'{num_}은(는) {n}자리수 입니다.')