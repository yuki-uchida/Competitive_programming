# RE TLE
import itertools
N, M = map(int, input().split())
if N % 2 == 0:
    points = [0 for _ in range(int((N + 1) * (N // 2)))]
else:
    points = [0 for _ in range(int((N + 1) * (N // 2) + ((N + 1) // 2)))]
groups = [list(map(int, input().split())) for _ in range(M)]
# print(len(points))
for a, b, x in groups:
    # 奇数は簡単
    if a % 2 == 1:
        point_a = (a) * ((a - 1) // 2) + b
    else:
        point_a = (a - 1) * ((a - 2) // 2) + ((a - 1) // 2) + b
    print(a, b, x, point_a)
    points[point_a - 1] += 1
    points[point_a] -= 1
    for i in range(a + 1, a + x + 1):
        if i % 2 == 1:
            point_b = (i) * ((i - 1) // 2) + b
            point_c = point_b + (i - a)
        else:
            # i=4
            point_b = (i) * ((i - 1) // 2) + (i // 2) + b
            point_c = point_b + (i - a)
        points[point_b - 1] += 1
        points[point_c] -= 1
    # print(point_a, point_b, point_c)
    # print(points)
# print(list(itertools.accumulate(points)))
print(len(list(filter(lambda x: x > 0, list(itertools.accumulate(points))))))
