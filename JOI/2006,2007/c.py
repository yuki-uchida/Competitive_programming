import math
# n <= 3000
# 3重for文だと10^9? ダメだろうな・・・
# でも、二点固定しただけだと対角線なのかわからない
N = int(input())
pillars = []
for i in range(N):
    pillars.append(tuple(map(int, input().split())))
# print(pillars)

pillars_set = set(pillars)
# 対角線の場合もある・・・・

# 反時計回りか時計回りを区別しないため、for文をi+1しない方が良い？？？
max_area = 0
for i in range(len(pillars) - 1):
    for j in range(i + 1, len(pillars)):
        x1, y1 = pillars[i]
        x2, y2 = pillars[j]
        x3, y3 = x1 + (y2 - y1), y1 + (x1 - x2)  # なんでここx1-x2じゃないんだ
        x4, y4 = x2 + (y2 - y1), y2 + (x1 - x2)
        if ((x3, y3) in pillars_set and (x4, y4) in pillars_set):
            # print([x1, y1], [x2, y2], [x3, y3], [x4, y4])
            max_area = max(max_area, (x2 - x1)**2 + (y2 - y1)**2)

print(max_area)
