records = [90, 85, 70, 55, 95, 60, 80, 90, 85, 70, 55, 95, 60, 80, 90, 85, 70, 55, 95, 60, 80]
l = len(records)
max_, min_ = -1, 9999
total_ = 0

for score in records:
    total_ += score
    if score > max_:
        max_ = score
    if score < min_:
        min_ = score

avg_ = total_

print('최고점 : ',  max_)
print('최저점 : ',  min_)
print('합계 : ',  total_)
print('평균 : ',  round(avg_,2))