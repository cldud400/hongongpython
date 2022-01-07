numbers = [273,103,5,32,65,9,72,800,99,100,-100,-9999]

for i in numbers:
    num_ = i
    i = abs(i)
    cnt = 0
    while True:
        i = (i // 10)
        cnt += 1
        if i == 0:
            break
    print(f'{num_}은(는) {cnt}자리수 입니다.')


