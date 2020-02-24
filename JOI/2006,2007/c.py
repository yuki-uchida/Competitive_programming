import math
N = int(input())
pillars = []
for i in range(N):
    pillars.append(list(map(int, input().split(" "))))
print(pillars)


# 対角線の場合もある・・・・
max_area = 0
for i in range(len(pillars)):
    for j in range(i + 1, len(pillars)):

print(max_area)
